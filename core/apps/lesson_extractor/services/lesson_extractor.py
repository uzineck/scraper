from dataclasses import dataclass
from abc import ABC, abstractmethod

from openpyxl.worksheet.worksheet import Worksheet

from core.apps.lesson_extractor.services.lesson_parser import LessonParserService
from core.common.utils import Utils


@dataclass
class BaseLessonExtractor(ABC):
    sheet: Worksheet

    @staticmethod
    @abstractmethod
    def get_lesson(sheet: Worksheet, column:int, row: int):
        ...


class LessonExtractorService(BaseLessonExtractor):
    @staticmethod
    def get_lesson(sheet: Worksheet, column: int, row: int):

        cell = sheet.cell(column=column, row=row)
        cell_value = cell.value

        if cell_value is None:
            merged_cell = Utils.is_merged_cell(sheet=sheet, cell=cell)
            if merged_cell:
                return merged_cell.start_cell.value  # LessonParserService.split_lesson_string(merged_cell.start_cell.value)
            else:
                return None
        else:
            return cell_value  # LessonParserService.split_lesson_string(cell_value)

