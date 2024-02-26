from core.common.constants import BOOK_NAMES


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