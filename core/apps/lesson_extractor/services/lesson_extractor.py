from dataclasses import dataclass
from abc import ABC, abstractmethod
from collections import defaultdict

from openpyxl.worksheet.worksheet import Worksheet

from core.apps.daysNnumbers.entities.classes_count import ClassNumberCoordinates
from core.apps.groups.entities.group import GroupCoordinates
from core.apps.lesson_extractor.services.lesson_parser import LessonParserService
from core.common.utils import Utils


@dataclass
class BaseLessonExtractor(ABC):
    sheet: Worksheet

    @staticmethod
    @abstractmethod
    def get_lesson(sheet: Worksheet, column: int, row: int):
        ...


class LessonExtractorService(BaseLessonExtractor):
    @staticmethod
    def get_lesson(sheet: Worksheet, column: int, row: int):

        cell = sheet.cell(column=column, row=row)
        cell_value = cell.value

        if cell_value is None:
            merged_cell = Utils.is_merged_cell(sheet=sheet, cell=cell)
            if merged_cell:
                return LessonParserService().parse_string(string=merged_cell.start_cell.value)
            else:
                return None
        else:
            return LessonParserService().parse_string(string=cell_value)

    def get_lessons_from_sheet(self, groups_from_sheet: dict, classes_count_of_sheet: dict):

        classes = defaultdict(lambda: defaultdict(dict))

        for group_key, group_coords in groups_from_sheet.items():
            for day_key, count_of_classes_with_coords in classes_count_of_sheet.items():
                for number_of_class, number_of_class_coords in count_of_classes_with_coords.items():
                    lessons = self._get_lessons_for_group(
                        number_of_class_coords,
                        group_coords,
                    )
                    classes[group_key][day_key][number_of_class] = lessons

        return classes

    def _get_lessons_for_group(self, number_of_class_coords: ClassNumberCoordinates, group_coords: GroupCoordinates):
        number_start_row, number_end_row = number_of_class_coords.start_row, number_of_class_coords.end_row

        group_start_column, group_end_column = group_coords.start_column, group_coords.end_column

        if group_start_column != group_end_column:
            return self._get_lessons_for_subgroup(
                group_start_column=group_start_column,
                group_end_column=group_end_column,
                number_start_row=number_start_row,
                number_end_row=number_end_row,
            )
        else:
            return self._get_lessons_for_single_column(
                group_start_column=group_start_column,
                number_start_row=number_start_row,
                number_end_row=number_end_row,
            )

    def _get_lessons_for_subgroup(self,
                                  group_start_column: int,
                                  group_end_column: int,
                                  number_start_row: int,
                                  number_end_row: int,
                                  ):

        lesson_a_1 = self.get_lesson(sheet=self.sheet, column=group_start_column, row=number_start_row)
        lesson_a_2 = self.get_lesson(sheet=self.sheet, column=group_start_column, row=number_end_row)
        lesson_b_1 = self.get_lesson(sheet=self.sheet, column=group_end_column, row=number_start_row)
        lesson_b_2 = self.get_lesson(sheet=self.sheet, column=group_end_column, row=number_end_row)

        return {
            "A": {"Numerator": lesson_a_1, "Denominator": lesson_a_2},
            "B": {"Numerator": lesson_b_1, "Denominator": lesson_b_2},
        }

    def _get_lessons_for_single_column(self,
                                       group_start_column: int,
                                       number_start_row: int,
                                       number_end_row: int,
                                       ):

        if number_start_row != number_end_row:
            lesson_1 = self.get_lesson(sheet=self.sheet, column=group_start_column, row=number_start_row)
            lesson_2 = self.get_lesson(sheet=self.sheet, column=group_start_column, row=number_end_row)
            return {"Numerator": lesson_1, "Denominator": lesson_2}
        else:
            lesson = self.get_lesson(sheet=self.sheet, column=group_start_column, row=number_start_row)
            return {"Numerator": lesson, "Denominator": lesson}

