from dataclasses import dataclass


@dataclass
class Coords:
    Column: int
    Row: int


@dataclass
class StartCoordinates(Coords):
    ...


@dataclass
class EndCoordinates(Coords):
    ...
