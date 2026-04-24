MatchType = str
AppName = str
MatchRe = str
MatchRegistry = dict[MatchType, dict[AppName, list[MatchRe]]]

MATCH_REGISTRY: MatchRegistry = {
    "app_id": {
        "code": ["code-url-handler", "code-oss"],
        "obsidian": ["obsidian"],
        "darktable": ["Darktable"],
        "gimp": [r"Gimp-\d+\.\d+"],
        "inkscape": [r"org\.inkscape\.Inkscape"],
        "ghostty": [r"com\.mitchellh\.ghostty"],
        "brave": ["brave-browser"],
        "chrome": ["chromium"],
        "firefox": ["firefox"],
        "discord": ["discord"],
    }
}
