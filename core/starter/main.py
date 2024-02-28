import time

from openpyxl.worksheet.worksheet import Worksheet

from workbook_loader import wb

from core.apps.bounds.services.coordinates import BoundsService
from core.apps.groups.services.groups import GroupsService
from core.apps.daysNnumbers.services.days import DaysService
from core.apps.daysNnumbers.services.classes_count import ClassesCountService
from core.apps.lesson_extractor.services.lesson_extractor import LessonExtractorService
from core.apps.lesson_extractor.services.lesson_parser import LessonParserService
from core.starter.json_dumper import JsonDumper

def main(sheet: Worksheet, sheet_name: str):
    bounds_coords = BoundsService(sheet=sheet, sheet_name=sheet_name).find_sheet_bounds()
    groups_coords = GroupsService(sheet=sheet).get_groups_from_sheet(bounds_coordinates=bounds_coords)
    days_coords = DaysService(sheet=sheet).get_days_from_sheet(bounds_coordinates=bounds_coords)
    classes_count = (ClassesCountService(sheet=sheet, sheet_name=sheet_name)
                     .get_number_of_classes_for_sheet(days_coordinates=days_coords))

    lessons = LessonExtractorService(sheet=sheet).get_lessons_from_sheet(groups_from_sheet=groups_coords,
                                                                         classes_count_of_sheet=classes_count)
    return lessons


if __name__ == "__main__":
    # for sheet_name in wb.sheetnames:
    #     sheet = wb[sheet_name]
    #     print(f'{sheet_name}: ', main(sheet=sheet, sheet_name=sheet_name))

    sheet_name = '2 курс'
    sheet = wb[sheet_name]

    start = time.monotonic()

    JsonDumper.dump(dict_data=main(sheet=sheet, sheet_name=sheet_name), filename=sheet_name)

    print(f'Time for program: {time.monotonic() - start}')
