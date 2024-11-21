from enum import Enum


class BOOK_NAMES(Enum):
    ENG_SHEET_NAMES = ('China 1 хвиля', 'China 2 хвиля', 'Turkey')


class EXCEPTION_VALUES(Enum):
    SHEET_NAME_EXCEPTIONS = ('4201-4202', '5201-5202', '6201-6202')
    GROUP_ROW_VALUES = ('Ауд.', 'AUD.', 'День', 'DAY', 'Пари', 'LES.')


class CHECK_VALUES(Enum):
    TEACHERS_RANKS = ('доц. (б.в.з.)', 'доц.(б.в.з.)', 'доц. б.в.з.', 'доц.б.в.з.', 'доц.',
                      'проф. (б.в.з.)', 'проф.(б.в.з.)', 'проф. б.в.з.', 'проф.б.в.з.', 'проф.',
                      'б.в.з.',
                      'ст. викл.', 'ст.викл.', 'викл.',
                      'асп.',
                      'senior lecturer', 'lecturer',
                      'associate professor', 'professor',)
