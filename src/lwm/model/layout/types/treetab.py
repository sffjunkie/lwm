from pydantic import BaseModel


from lwm.model.layout.types.typedef import Margin


class TreeTabLayout(BaseModel):
    active_bg: str = "#000080"
    active_fg: str = "base07"
    bg_color: str = "base07"
    border_width: int = 1
    font: str = "sans"
    fontshadow: str | None = None
    fontsize: int = 14
    inactive_bg: str = "#606060"
    inactive_fg: str = "#ffffff"
    level_shift: int = 8
    padding_left: int = 6
    padding_x: int = 6
    padding_y: int = 2
    panel_width: int = 150
    place_right: bool = False
    previous_on_rm: bool = False
    section_bottom: int = 6
    section_fg: str = "#ffffff"
    section_fontsize: int = 14
    section_left: int = 4
    section_padding: int = 4
    section_top: int = 4
    sections: list[str] = ["Default"]
    urgent_bg: str = "#ff0000"
    urgent_fg: str = "#ffffff"
    vspace: int = 2
