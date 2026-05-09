from pydantic import BaseModel


class NotifierDefs(BaseModel):
    general: str = "libnotify"
    music_track_change: str = "music-notify"
