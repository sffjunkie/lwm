from pydantic import BaseModel


class PhysicalSize(BaseModel):
    width: int
    height: int


class OutputMode(BaseModel):
    width: int
    height: int
    refresh: float
    preferred: bool
    current: bool


class OutputPosition(BaseModel):
    x: int
    y: int


class Output(BaseModel):
    name: str
    description: str
    make: str
    model: str
    serial: str
    physical_size: PhysicalSize
    enable: bool
    modes: list[OutputMode]
    position: OutputPosition
    transform: str
    scale: float
    adaptive_sync: bool


class Outputs(BaseModel):
    outputs: list[Output]
