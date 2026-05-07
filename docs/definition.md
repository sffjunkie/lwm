
# Definitions

- Defines how the [Looniversity Window Manager](../README.md) works.
- Uses TOML files

## `app.toml`

Defines applications to be used by the window manager

```toml
[app]
terminal = "ghostty"  # terminal to be used
launcher = "rofi-app-launcher"  # used to launch applications
etc...
```

## `bar.toml`

Currently only configures height, opacity, and margins.

## `color.toml`

If `scheme_dir` and `scheme_name` are defined then the base16 colors are loaded
from the scheme file in the scheme directory.

`color.base16.colors` allows you to override individual base16 hex colors

`color.named` associates a name with either a hex color or a base16 reference.

```toml
[color]
[color.base16]
scheme_dir = "<path to schemes directory>"
scheme_name = "e.g. catppuccin-macchiato"
[color.base16.colors]
base00 = "#24273a"

[color.named]
widget_bg = "base0f"
```

## `controller.toml`

Defines applications to control the system.

```toml
[controller]
audio = "pavucontrol"  # Controls audio playback/routing
music = "musicctl"  # Controls music playback (play, stop etc.)
volume = "volumectl"  # Controls audio volume (mute, raise, lower etc.)
```

## `device.toml`

Currently only defines network devices.

```toml
wifi = "wlp1s1"
eth = "eth0"
```

## `floating.toml`

Defines which windows are floated.

```toml
[floating]
matches = [ "appname" ]
```

where `appname` matches a name defined in [match.toml](#matchtoml)

## `font.toml`

Configures font families and sizes

```toml
[font]
[font.text]
family = "JetBrainsMono Nerd Font"
size = 16
```

## `group.toml`

Defines [Qtile Groups](https://docs.qtile.org/en/latest/manual/config/groups.html)

```toml
[group]
decoration = "superscript"  # decoration to show after the group name
layout = "max"  # The default layout to use for a group

[[group.defs]]  # List of group definitions
name = "WWW"  # group name
layout = "monadtall"  # default layout
matches = ["brave", "chrome", "firefox"]  # Match names
```

where the names in matches match one of those defined in [match.toml](#matchtoml)

## `key.toml`

```toml
[key]
[key.modifier]  # Associates a key name with an X11 style modifier bit name
alt = "mod1"
cmd = "mod4"
ctrl = "control"
hyper = "mod3"
shift = "shift"

[key.modifier_group] # Associates a name with a list of key names
switch_window = ["cmd"]

[[key.defs]]  # List of key definitions
```

### Key Definition

```toml
[[key.defs]]
key = "F1"
modifier_group = "launch_app"
command = "lwm:spawn:menu.user"
desc = "Show the user menu"
```

- `key` is a Qtile key name
- `modifier_group` is a modifier group as defined above
- `command` a command string as defined below
- `desc` a description of the key command

### Command Strings

Command strings are of the form

```none
class:function:arguments
```

Where

- `class` is either `qtile` or `lwm`
- `function` is a Qtile lazy function
- `arguments` are the arguments to the function separated by commas
  - for `qtile` commands arguments are passed directly to the function
  - for `lwm` commands the first argument is used to retrieve a value from an
    lwm definition e.g. `lwm:spawn:app.launcher`

For `lwm` functions only `spawn` is supported.

Examples

- `qtile:layout.grow_main` - Calls `lazy.layout.grow_main()`
- `qtile:core.change_vt:1` - Calls `lazy.layout.core.change_vt(1)`
- `lwm:spawn:app.code_editor` -  If `code_editor = "code"` is set in `app.toml`
  then `lazy.spawn("code")` will be called.

## `layout.toml`

```toml
[layout]
[layout.base]  # default layout values if not specifically specified 
border_width = 4
margin = 8
rounded = true  # Display with rounded corners

[layout.defs.monadtall]
...
```

## `match.toml`

Defines how to determine if a window is shown on a specific group or floated.

```toml
[match.defs]
waypaper = [{ appid = "waypaper" }]
vscode = [{ appid = "code" }, { appid = "code-url-handler" }]
orca-slicer-saveas = [{ appid = "orca-slicer", title = "Save file as" }]
```
