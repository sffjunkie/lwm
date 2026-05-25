from pydantic import BaseModel


class ColumnsLayout(BaseModel):
    align: int = 1
    border_focus: str = "#881111"
    border_focus_stack: str = "#881111"
    border_normal: str = "#220000"
    border_normal_stack: str = "#220000"
    border_on_single: bool = False
    border_width: int = 2
    fair: bool = True
    grow_amount: int = 10
    initial_ratio: int = 1
    insert_position: int = 0
    margin: int = 0
    margin_on_single: list | None = None
    num_columns: int = 2
    single_border_width: int | None = None
    split: bool = True
    wrap_focus_columns: bool = True
    wrap_focus_rows: bool = True
    wrap_focus_stacks: bool = True
