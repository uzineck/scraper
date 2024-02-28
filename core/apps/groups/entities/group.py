from dataclasses import dataclass
from typing import TypeAlias, Dict

from core.common.entities import ColumnCoordinates

Group: TypeAlias = str


@dataclass
class GroupCoordinates(ColumnCoordinates):
    ...

GroupCoords: dict[Group, GroupCoordinates]

