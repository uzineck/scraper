from dataclasses import dataclass
from typing import TypeAlias

from core.common.entities import RowCoordinates

Day: TypeAlias = str


@dataclass
class DayCoordinates(RowCoordinates):
    ...
