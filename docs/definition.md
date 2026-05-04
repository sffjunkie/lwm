
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

```toml
[color]
[color.base16]
scheme_dir = "<path to schemes directory>"
scheme_name = "e.g. catppuccin-macchiato"
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

## `layout.toml`

```toml
[layout]
[layout.defs.base]  # default layout values
border_width = 4
margin = 8
rounded = true  # Display with rounded corners

[layout.defs.monadtall]
...
```

## `match.toml`

```toml
```
