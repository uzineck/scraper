from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell import Cell, MergedCell

from core.common.constants import BOOK_NAMES


class Utils:
    @staticmethod
    def is_merged_cell(sheet: Worksheet, cell: Cell) -> MergedCell | bool:
        cell_coordinate = cell.coordinate
        if cell_coordinate in sheet.merged_cells:
            for merged_cell in sheet.merged_cells.ranges:
                if cell_coordinate in merged_cell:
                    return merged_cell
        return False

    @staticmethod
    def get_target_word(column: int, sheet_name: str) -> tuple | str:
        target_word_urk_dict = {1: 'День', 2: 'Пари'}
        target_word_eng_dict = {1: 'DAY', 2: 'LES.'}

        try:
            target_word_urk = target_word_urk_dict[column]
            target_word_eng = target_word_eng_dict[column]

            target_word = target_word_eng if sheet_name in BOOK_NAMES.ENG_SHEET_NAMES.value else target_word_urk
            return target_word

        except KeyError:
            raise ValueError(f"Invalid column value: {column}. "
                             f"Use only 1 for the first column with days"
                             f" and 2 for the second column with lesson numbers.")
