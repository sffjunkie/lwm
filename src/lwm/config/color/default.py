from lwm.config.color.typedef import Base16Colors, Colors, NamedColors

# Catppuccin Macchiato
DEFAULT_BASE16_COLORS: Base16Colors = {
    "base00": "#24273a",  # base
    "base01": "#1e2030",  # mantle
    "base02": "#363a4f",  # surface0
    "base03": "#494d64",  # surface1
    "base04": "#5b6078",  # surface2
    "base05": "#cad3f5",  # text
    "base06": "#f4dbd6",  # rosewater
    "base07": "#b7bdf8",  # lavender
    "base08": "#ed8796",  # red
    "base09": "#f5a97f",  # peach
    "base0a": "#eed49f",  # yellow
    "base0b": "#a6da95",  # green
    "base0c": "#8bd5ca",  # teal
    "base0d": "#8aadf4",  # blue
    "base0e": "#c6a0f6",  # mauve
    "base0f": "#f0c6c6",  # flamingo
}


DEFAULT_NAMED_COLORS: NamedColors = {
    "panel_fg": "base01",
    "panel_bg": "base0f",
    "group_current_fg": "base05",
    "group_current_bg": "base0f",
    "group_active_fg": "base01",
    "group_active_bg": "base09",
    "group_inactive_fg": "base03",
    "group_inactive_bg": "base03",
    "widget_bg": ["base06"],
    "widget_fg_dark": "base00",
    "widget_fg_light": "base01",
    "window_border_focus": "base0f",
    "window_border_normal": "base01",
}


DEFAULT_COLORS: Colors = {
    "base16": DEFAULT_BASE16_COLORS,
    "named": DEFAULT_NAMED_COLORS,
}
