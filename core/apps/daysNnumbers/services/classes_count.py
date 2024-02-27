from dataclasses import dataclass
from abc import ABC, abstractmethod

from openpyxl.worksheet.worksheet import Worksheet

from core.common.utils import Utils
from core.apps.bounds.services.coordinates import BoundsService
from core.apps.bounds.entities.coordinates import StartCoordinates
from core.apps.daysNnumbers.entities.days import Day, DayCoordinates
from core.apps.daysNnumbers.entities.classesc_count import ClassNumber, ClassNumberCoordinates


@dataclass
class BaseClassesCount(ABC):
    sheet: Worksheet
    sheet_name: str

    @abstractmethod
    def get_number_of_classes_for_sheet(self,
                                        days_coordinates: tuple[int, int],
                                        ) -> dict[Day, dict[ClassNumber, ClassNumberCoordinates]]:
        ...

    @abstractmethod
    def get_number_of_classes_for_day(self,
                                      bound_start_coordinates: StartCoordinates,
                                      day_coordinates: DayCoordinates,
                                      ):
        ...


class ClassesCountService(BaseClassesCount):

    def get_number_of_classes_for_sheet(self,
                                        days_coordinates: dict[Day, DayCoordinates],
                                        ) -> dict[Day, dict[ClassNumber, ClassNumberCoordinates]]:

        classes_count = {}

        target_word = Utils.get_target_word(column=2, sheet_name=self.sheet_name)
        start_coords = BoundsService.find_start_coordinates(sheet=self.sheet, target_word=target_word)

        for day, day_coordinates in days_coordinates.items():
            classes_count[day] = self.get_number_of_classes_for_day(tw_start_coordinates=start_coords,
                                                                    day_coordinates=day_coordinates, )
        return classes_count

    def get_number_of_classes_for_day(self,
                                      tw_start_coordinates: StartCoordinates,
                                      day_coordinates: DayCoordinates,
                                      ) -> dict[ClassNumber, ClassNumberCoordinates]:

        class_count = {}

        day_start_row, day_end_row = day_coordinates.start_row, day_coordinates.end_row
        tw_start_column, tw_start_row = tw_start_coordinates.Column, tw_start_coordinates.Row

        for row_coord in range(day_start_row, day_end_row + 1):
            cell = self.sheet.cell(row=row_coord, column=tw_start_column)
            cell_value = cell.value
            cell_row = cell.row

            if cell_value is not None:
                merged_cell = Utils.is_merged_cell(sheet=self.sheet, cell=cell)
                max_row_in_merge = merged_cell.max_row if merged_cell else cell_row

                class_count[int(cell_value)] = ClassNumberCoordinates(cell_row, max_row_in_merge)

        return class_count
