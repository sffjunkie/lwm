from pydantic import BaseModel

from lwm.model.layout.types.typedef import Margin, ClientPosition


class MonadTallLayout(BaseModel):
    align: int = 0
    auto_maximise: bool = False
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 2
    change_ratio: float = 0.5
    change_size: int = 20
    margin: int | Margin = 2
    max_ratio: float = 0.75
    min_ratio: float = 0.25
    min_secondary_size: int = 85
    new_client_position: ClientPosition = ClientPosition.after_current
    ratio: float = 0.5
    single_border_width: int | None = None
    single_margin: int | None = None


class MonadThreeColLayout(BaseModel):
    align: int = 0
    auto_maximise: bool = False
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 2
    change_ratio: float = 0.5
    change_size: int = 20
    main_centered: bool = True
    margin: int | Margin = 4
    max_ratio: float = 0.75
    min_ratio: float = 0.25
    min_secondary_size: int = 85
    new_client_position: ClientPosition = ClientPosition.after_current
    ratio: float = 0.5
    single_border_width: int | None = None
    single_margin: int | None = None


class MonadWideLayout(BaseModel):
    align: int = 0
    auto_maximise: bool = False
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 2
    change_ratio: float = 0.5
    change_size: int = 20
    main_centered: bool = True
    margin: int | Margin = 4
    max_ratio: float = 0.75
    min_ratio: float = 0.25
    min_secondary_size: int = 85
    new_client_position: ClientPosition = ClientPosition.after_current
    ratio: float = 0.5
    single_border_width: int | None = None
    single_margin: int | None = None
