from collections import defaultdict

from openpyxl import load_workbook
from openpyxl import Workbook

from core.bounds.services.coordinates import BoundsService


path_1_sem = 'D:/pythonwork/1sem.xlsx'
path_2_sem = 'D:/pythonwork/2sem.xlsx'


wb: Workbook = load_workbook(path_2_sem)

sheet_name = '1 курс'
sheet = wb[sheet_name]

if __name__ == "__main__":
    all_bounds = {}
    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        bounds = BoundsService(sheet=sheet, sheet_name=sheet_name).find_sheet_bounds()
        all_bounds[sheet_name] = bounds
    print(all_bounds)

