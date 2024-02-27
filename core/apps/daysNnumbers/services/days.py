from dataclasses import dataclass
from abc import ABC, abstractmethod

from openpyxl.worksheet.worksheet import Worksheet

from core.apps.daysNnumbers.entities.days import Day, DayCoordinates
from core.apps.bounds.entities.coordinates import StartCoordinates, EndCoordinates
from core.common.utils import Utils


@dataclass
class BaseDays(ABC):
    sheet: Worksheet

    @abstractmethod
    def get_days_from_sheet(self,
                            bounds_coordinates: tuple[StartCoordinates, EndCoordinates],
                            ) -> dict[Day, DayCoordinates]:
        ...

    @abstractmethod
    def extract_days_from_sheet(self, start_row: int, end_row: int, days_column: int):
        ...


class DaysService(BaseDays):

    def get_days_from_sheet(self,
                            bounds_coordinates: tuple[StartCoordinates, EndCoordinates],
                            ) -> dict[Day, DayCoordinates]:
        start_coords, end_coords = bounds_coordinates

        start_column, start_row = start_coords.Column, start_coords.Row
        end_column, end_row = end_coords.Column, end_coords.Row

        days = self.extract_days_from_sheet(start_row=start_row, end_row=end_row, days_column=start_column)

        return days

    def extract_days_from_sheet(self, start_row: int, end_row: int, days_column: int):
        days = {}

        for row_coord in range(start_row, end_row):
            cell = self.sheet.cell(row=row_coord, column=days_column)
            cell_value: Day = cell.value

            if cell_value is not None:
                merged_cell = Utils.is_merged_cell(sheet=self.sheet, cell=cell)

                if merged_cell:
                    days[cell_value] = DayCoordinates(cell.row, merged_cell.max_row)

        return days

