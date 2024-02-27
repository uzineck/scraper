from dataclasses import dataclass


@dataclass
class ColumnCoordinates:
    start_column: int
    end_column: int


@dataclass
class RowCoordinates:
    start_row: int
    end_row: int
