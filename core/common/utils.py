from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell import Cell, MergedCell


class Utils:
    @staticmethod
    def is_merged_cell(sheet: Worksheet, cell: Cell) -> MergedCell | bool:
        cell_coordinate = cell.coordinate
        if cell_coordinate in sheet.merged_cells:
            for merged_cell in sheet.merged_cells.ranges:
                if cell_coordinate in merged_cell:
                    return merged_cell
        return False
