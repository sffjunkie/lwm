from pydantic import BaseModel


class Apps(BaseModel):
    brain: str = "obsidian"
    browser: str = "firefox"
    code_editor: str = "code"
    editor: str = "micro"
    file_manager: str = "ranger"
    launcher: str = "rofi-launcher"
    music_player: str = "ncmpcpp"
    pager: str = "bat"
    terminal: str = "ghostty"
