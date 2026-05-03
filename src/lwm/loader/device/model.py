from pydantic import BaseModel


class DeviceDefs(BaseModel):
    wifi: str | None = None
    eth: str | None = None
