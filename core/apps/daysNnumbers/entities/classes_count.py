from dataclasses import dataclass
from typing import TypeAlias

from core.common.entities import RowCoordinates

ClassNumber: TypeAlias = int


@dataclass
class ClassNumberCoordinates(RowCoordinates):
    ...
