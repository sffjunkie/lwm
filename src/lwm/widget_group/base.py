from typing import Protocol

from libqtile.widget import base

from lwm.context.widget_group import WidgetGroupContext


class WidgetGroup(Protocol):
    def __init__(
        self,
        ctx: WidgetGroupContext,
    ): ...

    def widgets(self, group_id: int = -1) -> list[base._Widget]: ...
