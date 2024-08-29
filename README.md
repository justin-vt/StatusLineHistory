# StatusLineHistory

This is a simple fork of https://github.com/AmedeeBulle/StatusLine that increases the number of status line messages to three and adds a timestamp.

![StatusLineHistory](status_line_history.png?raw=true)

Original readme continues below:

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/AmedeeBulle/StatusLine/archive/master.zip

## Configuration

If you want to move the plugin to appear at the top of the sidebar, modify the config.yaml file as follows:

```yaml
appearance:
  components:
    order:
      sidebar:
        - plugin_status_line
```
