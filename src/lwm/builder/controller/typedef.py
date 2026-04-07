from dataclasses import dataclass


@dataclass
class ClipboardController:
    clear: str
    copy: str
    delete: str


@dataclass
class MusicController:
    next: str
    play: str
    previous: str
    stop: str
    toggle: str


@dataclass
class VolumeController:
    down: str
    mute: str
    toggle: str
    up: str
