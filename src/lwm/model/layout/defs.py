from pydantic import BaseModel

from .base import LayoutBase
from .types.bsp import BspLayout
from .types.columns import ColumnsLayout
from .types.matrix import MatrixLayout
from .types.max import MaxLayout
from .types.monad import MonadTallLayout, MonadThreeColLayout, MonadWideLayout
from .types.plasma import PlasmaLayout
from .types.ratiotile import RatioTileLayout
from .types.spiral import SpiralLayout
from .types.stack import StackLayout
from .types.tile import TileLayout
from .types.treetab import TreeTabLayout
from .types.vertical import VerticalTileLayout
from .types.zoomy import ZoomyLayout


class LayoutType(BaseModel):
    bsp: BspLayout = BspLayout()
    columns: ColumnsLayout = ColumnsLayout()
    matrix: MatrixLayout = MatrixLayout()
    max: MaxLayout = MaxLayout()
    monadtall: MonadTallLayout = MonadTallLayout()
    monadthreecol: MonadThreeColLayout = MonadThreeColLayout()
    monadwide: MonadWideLayout = MonadWideLayout()
    plasma: PlasmaLayout = PlasmaLayout()
    ratiotile: RatioTileLayout = RatioTileLayout()
    spiral: SpiralLayout = SpiralLayout()
    stack: StackLayout = StackLayout()
    tile: TileLayout = TileLayout()
    treetab: TreeTabLayout = TreeTabLayout()
    verticaltile: VerticalTileLayout = VerticalTileLayout()
    zoomy: ZoomyLayout = ZoomyLayout()


class LayoutDefs(BaseModel):
    default_layouts: list[str] = ["max"]
    base: LayoutBase = LayoutBase()
    layouts: LayoutType = LayoutType()
