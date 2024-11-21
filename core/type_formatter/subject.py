import glob
import os

from core.type_formatter.json_loader import load_json, dump_set


def extract_from_schedule(directory_path, file_name):
    all_subjects = set()

    for filepath in glob.glob(os.path.join(directory_path, "*.json")):
        schedule_dict = load_json(filepath=filepath)

        for group in schedule_dict.values():
            for day in group.values():
                for number in day.values():
                    for subgroup in number.values():
                        if subgroup is not None:
                            for lesson in subgroup.values():
                                if lesson is not None and isinstance(lesson, dict):
                                    print(lesson)
                                    subject = lesson['Lesson']
                                    if isinstance(subject, list):
                                        all_subjects.update(subject)
                                    else:
                                        all_subjects.add(subject)

    dump_set(_set=all_subjects, filename=file_name)
    return all_subjects


extract_from_schedule(directory_path="../../json_schedules/1_sem/", file_name="subjects_2023_1_sem")
extract_from_schedule(directory_path="../../json_schedules/1sem", file_name="subjects_2024_1_sem")


