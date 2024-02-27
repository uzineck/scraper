from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Mapping

from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell.cell import Cell

from core.apps.groups.entities.group import Group, GroupCoordinates
from core.apps.bounds.entities.coordinates import StartCoordinates, EndCoordinates
from core.common.constants import EXCEPTION_VALUES
from core.common.utils import Utils


@dataclass
class BaseGroups(ABC):
    sheet: Worksheet

    @abstractmethod
    def get_groups_from_sheet(self,
                              bounds_coordinates: tuple[StartCoordinates, EndCoordinates],
                              ) -> Mapping[Group, GroupCoordinates]:
        ...


class GroupsService(BaseGroups):

    def get_groups_from_sheet(self,
                              bounds_coordinates: tuple[StartCoordinates, EndCoordinates],
                              ) -> dict[Group, GroupCoordinates]:

        start_coords, end_coords = bounds_coordinates

        start_column, start_row = start_coords.Column, start_coords.Row
        end_column, end_row = end_coords.Column, end_coords.Row

        groups = self.extract_groups_from_sheet(start_column=start_column, groups_row=start_row, end_column=end_column)

        return groups

    def extract_groups_from_sheet(self,
                                  start_column: int,
                                  end_column: int,
                                  groups_row: int,
                                  ) -> dict[Group, GroupCoordinates]:
        groups = {}

        for column in range(start_column, end_column):
            cell: Cell = self.sheet.cell(row=groups_row, column=column)
            cell_value: Group = cell.value
            cell_column = cell.column

            if cell_value is not None and cell_value not in EXCEPTION_VALUES.GROUP_ROW_VALUES.value:
                merged_cell = Utils.is_merged_cell(sheet=self.sheet, cell=cell)
                max_col_in_merge = merged_cell.max_col if merged_cell else cell_column

                groups = self.check_for_group_instance(groups, cell_value, cell_column, max_col_in_merge)

        return groups

    @staticmethod
    def check_for_group_instance(groups: dict, cell_value: Group, cell_column, max_col_in_merge):
        if isinstance(cell_value, (int, float)):
            groups[str(int(cell_value))] = GroupCoordinates(cell_column, max_col_in_merge)
        else:
            groups[cell_value] = GroupCoordinates(cell_column, max_col_in_merge)

        return groups
