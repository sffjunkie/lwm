from pydantic import BaseModel


class Devices(BaseModel):
    wifi: str | None = None
    eth: str | None = None
