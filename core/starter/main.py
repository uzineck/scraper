from openpyxl.worksheet.worksheet import Worksheet

from workbook_loader import wb

from core.apps.bounds.services.coordinates import BoundsService
from core.apps.groups.services.groups import GroupsService
from core.apps.daysNnumbers.services.days import DaysService
from core.apps.daysNnumbers.services.classes_count import ClassesCountService
from core.apps.lesson_extractor.services.lesson_extractor import LessonExtractorService
from core.apps.lesson_extractor.services.lesson_parser import LessonParserService


def main(sheet: Worksheet, sheet_name: str):
    # bounds_coords = BoundsService(sheet=sheet, sheet_name=sheet_name).find_sheet_bounds()
    # groups_coords = GroupsService(sheet=sheet).get_groups_from_sheet(bounds_coordinates=bounds_coords)
    # days_coords = DaysService(sheet=sheet).get_days_from_sheet(bounds_coordinates=bounds_coords)
    # classes_count = (ClassesCountService(sheet=sheet, sheet_name=sheet_name)
    #                 .get_number_of_classes_for_sheet(days_coordinates=days_coords))

    lesson = LessonParserService().parse_string(string="Друга іноземна мова"
                                                       "ст. викл. Пітерова Н.А.   , викл. Гаврилюк Д.М., доц. Вакуленко "
                                                       "Т.І., доц. Мозолевська А.С.")

    return lesson


if __name__ == "__main__":
    # for sheet_name in wb.sheetnames:
    #     sheet = wb[sheet_name]
    #     print(f'{sheet_name}: ', main(sheet=sheet, sheet_name=sheet_name))

    sheet_name = '1 курс'
    sheet = wb[sheet_name]
    print(main(sheet=sheet, sheet_name=sheet_name))
