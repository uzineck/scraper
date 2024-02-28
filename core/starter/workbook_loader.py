import time
from collections import defaultdict

from openpyxl import load_workbook
from openpyxl import Workbook


path_1_sem = 'D:/pythonwork/1sem.xlsx'
path_2_sem = 'D:/pythonwork/2sem.xlsx'

start = time.monotonic()
wb: Workbook = load_workbook(path_2_sem)
wb_load = time.monotonic() - start
print(f'Time for wb: {wb_load}\n')

