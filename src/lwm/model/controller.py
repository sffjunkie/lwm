from typing import Self

from pydantic import BaseModel, model_validator


class AudioController(BaseModel):
    app: str = "pavucontrol"


class ClipboardController(BaseModel):
    app: str = "rofi-clip"
    cmd_copy: str | None = None
    cmd_delete: str | None = None

    @model_validator(mode="after")
    def commands(self) -> Self:
        self.cmd_copy = self.cmd_copy or f"{self.app} copy"
        self.cmd_delete = self.cmd_delete or f"{self.app} delete"
        return self


class MusicController(BaseModel):
    app: str = "musicctl"
    cmd_toggle: str | None = None
    cmd_stop: str | None = None
    cmd_next: str | None = None
    cmd_previous: str | None = None

    @model_validator(mode="after")
    def commands(self) -> Self:
        self.cmd_toggle = self.cmd_toggle or f"{self.app} toggle"
        self.cmd_stop = self.cmd_stop or f"{self.app} stop"
        self.cmd_next = self.cmd_next or f"{self.app} next"
        self.cmd_previous = self.cmd_previous or f"{self.app} previous"
        return self


class VolumeController(BaseModel):
    app: str = "volumectl"
    cmd_toggle: str | None = None
    cmd_up: str | None = None
    cmd_down: str | None = None
    cmd_mute: str | None = None

    @model_validator(mode="after")
    def commands(self) -> Self:
        self.cmd_toggle = self.cmd_toggle or f"{self.app} toggle"
        self.cmd_up = self.cmd_up or f"{self.app} up"
        self.cmd_down = self.cmd_down or f"{self.app} down"
        self.cmd_mute = self.cmd_mute or f"{self.app} mute"
        return self


class ControllerDefs(BaseModel):
    audio: AudioController = AudioController()
    clipboard: ClipboardController = ClipboardController()
    music: MusicController = MusicController()
    volume: VolumeController = VolumeController()
