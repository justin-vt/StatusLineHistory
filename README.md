# StatusLineHistory

This is a simple fork of https://github.com/AmedeeBulle/StatusLine that increases the number of status line messages to three and adds a timestamp.

![StatusLineHistory](status_line_history.png?raw=true)

## Setup

Install manually using this URL:

    https://github.com/justin-vt/StatusLineHistory/archive/master.zip

## Configuration

If you want to move the plugin to appear at the top of the sidebar, modify the config.yaml file as follows (or use the excellent [UI Customizer](https://github.com/LazeMSS/OctoPrint-UICustomizer)):

```yaml
appearance:
  components:
    order:
      sidebar:
        - plugin_status_line_history
```
