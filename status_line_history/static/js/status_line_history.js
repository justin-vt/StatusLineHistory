
$(function() {
    function StatusLineHistoryViewModel(parameters) {
        var self = this;

        self.status_line_history = ko.observableArray([]);
        self.show_status = ko.observable(false);

        self.initialMessage = function(data) {
            console.log("StatusLineHistory: Initial data received", data);
            self.status_line_history(data.status_line_history);
            self.show_status(data.status_line_history.length > 0);
        };

        self.onStartupComplete = function() {
            console.log("StatusLineHistory: onStartupComplete - Fetching initial data");
            $.ajax({
                url: API_BASEURL + "plugin/status_line_history",
                type: "GET",
                dataType: "json",
                success: self.initialMessage,
                error: function(jqXHR, textStatus, errorThrown) {
                    console.error("StatusLineHistory: Error fetching initial data", textStatus, errorThrown);
                }
            });
        }

        self.onDataUpdaterPluginMessage = function(plugin, data) {
            if (plugin != "status_line_history") {
                return;
            }
            console.log("StatusLineHistory: Plugin message received", data);
            self.status_line_history(data.status_line_history);
            self.show_status(true);
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: StatusLineHistoryViewModel,
        dependencies: [],
        elements: ["#status_line_history"]  // Corrected the binding target
    });
});
