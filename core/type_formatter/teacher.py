import glob
import os

from core.common.constants import CHECK_VALUES
from core.type_formatter.json_loader import load_json, dump_set


def flatten(lst):
    """Flattens a list, handling any level of nested lists."""
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))  # Recursively flatten the list
        else:
            flattened_list.append(item)
    return flattened_list


def check_rank_exclude(teacher_set):
    updated_teachers = set()
    for teacher in teacher_set:
        for rank in CHECK_VALUES.TEACHERS_RANKS.value:
            if rank in teacher:
                teacher = teacher.replace(rank, '').strip()
        updated_teachers.add(teacher)
    return updated_teachers


def check_for_removal(teacher_set):
    updated_teachers = set()
    for teacher in teacher_set:
        if '(' in teacher:
            teacher = teacher.split('(')[0]
        if '+' in teacher:
            teacher = teacher.split('+')[0]
        try:
            teacher = int(teacher)
            teacher = str(teacher).replace(str(teacher), '')
        except ValueError:
            pass
        updated_teachers.add(teacher)
    return updated_teachers


def extract_from_schedule(directory_path, file_name):
    all_teachers = set()

    for filepath in glob.glob(os.path.join(directory_path, "*.json")):
        schedule_dict = load_json(filepath=filepath)

        for group in schedule_dict.values():
            for day in group.values():
                for number in day.values():
                    for subgroup in number.values():
                        if subgroup is not None:
                            for lesson in subgroup.values():
                                if lesson is not None and isinstance(lesson, dict):
                                    teacher = lesson['Teacher']
                                    if isinstance(teacher, list):
                                        all_teachers.update(flatten(teacher))
                                    else:
                                        all_teachers.add(teacher)
    updated_teachers = check_rank_exclude(all_teachers)
    updated_teachers = check_rank_exclude(updated_teachers)
    updated_teachers = check_for_removal(updated_teachers)
    dump_set(_set=updated_teachers, filename=file_name)
    return updated_teachers


print(extract_from_schedule(directory_path="../../json_schedules/1_sem/", file_name="teachers_2023_1_sem"))
