from dataclasses import dataclass
from typing import TypeAlias

from core.common.entities import ColumnCoordinates

Group: TypeAlias = str


@dataclass
class GroupCoordinates(ColumnCoordinates):
    ...

