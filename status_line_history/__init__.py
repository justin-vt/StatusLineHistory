
# coding=utf-8
from __future__ import absolute_import

import flask
import octoprint.plugin
from datetime import datetime

class StatusLineHistoryPlugin(octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.SimpleApiPlugin,
                       octoprint.plugin.OctoPrintPlugin
                       ):

    def __init__(self):
        self.messages = []

    # OctoPrintPlugin hook
    def hook_m117(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        if gcode and gcode == "M117":
            message = cmd[5:]
            timestamp = datetime.now().strftime("%I:%M:%S %p")
            formatted_message = {"timestamp": timestamp, "message": message}
            self._logger.info("StatusLineHistory: Captured M117 message: {0}".format(formatted_message))
            self.messages.append(formatted_message)
            if len(self.messages) > 3:
                self.messages.pop(0)
            self._logger.info("StatusLineHistory: Current message list: {0}".format(self.messages))
            self._plugin_manager.send_plugin_message(self._identifier, dict(status_line_history=self.messages))
            self._logger.info("StatusLineHistory: Sent message list to frontend")

    # AssetPlugin
    def get_assets(self):
        return {
            "js": ["js/status_line_history.js"],
            "css": ["css/status_line_history.css"]
        }

    # TemplatePlugin
    def get_template_configs(self):
        return [
            dict(type="sidebar", name="Status Line History", icon="print")
        ]

    # SimpleApiPlugin
    def on_api_get(self, request):
        self._logger.info("StatusLineHistory: API request received")
        return flask.jsonify(dict(
            status_line_history=self.messages or [{"timestamp": "", "message": "No messages"}]
        ))

__plugin_name__ = "Status Line History"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = StatusLineHistoryPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.sent": __plugin_implementation__.hook_m117
    }
