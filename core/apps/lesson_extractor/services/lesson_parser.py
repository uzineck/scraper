import re

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from core.common.constants import CHECK_VALUES

# TODO parser additional info logic because it conflicts with teacher rank in parenthesis


@dataclass
class BaseLessonParser(ABC):
    teacher_ranks: CHECK_VALUES.TEACHERS_RANKS = field(default=CHECK_VALUES.TEACHERS_RANKS.value)

    @abstractmethod
    def parse_string(self, string: str):
        ...


class LessonParserService(BaseLessonParser):
    rank_pattern = None

    def __init__(self):
        if LessonParserService.rank_pattern is None:
            LessonParserService.rank_pattern = '|'.join(re.escape(rank) for rank in self.teacher_ranks)

    def parse_string(self, string: str):
        if string is None:
            return string
        if "/" not in string:
            return self.parse_string_without_additions(string=string)
        if "/" in string:
            return self.parse_slash_string(string=string)

    def parse_string_without_additions(self, string: str):
        matches = re.finditer(self.rank_pattern, string)

        indexes = [match.start() for match in matches]

        divider = min(indexes) if indexes else len(string)

        lesson = string[:divider].replace("\n", "").strip()
        teacher = string[divider:].replace("\n", "").strip()

        teacher = self._teachers_scenario(teacher=teacher)

        return {"Lesson": lesson,
                "Teacher": teacher}

    def parse_slash_string(self, string: str):
        string_list = string.split('/')

        lessons = []
        teachers = []

        for string in string_list:
            lesson_teacher_dict = self.parse_string_without_additions(string=string)
            lessons.append(lesson_teacher_dict["Lesson"])
            teachers.append(lesson_teacher_dict["Teacher"])

        return {"Lesson": lessons,
                "Teacher": teachers}

    @staticmethod
    def _teachers_scenario(teacher: str):
        if "," not in teacher:
            return teacher.strip()

        teachers = re.split(r',(?![^(]*\))', teacher)
        return [teacher.strip() for teacher in teachers]

    def _lesson_type_scenario(self, lesson: str | list):
        lesson_type = re.search(r'(.+):', lesson)

        if not lesson_type:
            return False, lesson

        lesson_type = lesson_type.group(1)
        lesson = lesson.replace(f"{lesson_type}:", "")
        return lesson_type, lesson

    def _additional_info_scenario(self, teacher: str):
        additional_info = []

        additional_info_pattern = re.search(r'\(([^()]+)\)', teacher)
        if additional_info_pattern and additional_info_pattern.group(1) not in self.teacher_ranks:

            additional_info.append(additional_info_pattern.group(1))
            teacher = teacher.replace(f"({additional_info_pattern.group(1)})", "").strip()

        if "+" in teacher:
            index = teacher.find("+")
            other_groups = teacher[index + 1:].strip().split(", ") or teacher[index + 1:].strip().split(",")
            additional_info.append(other_groups)
            teacher = teacher.split("+")[0].strip()

        if not additional_info:
            return False, teacher

        return additional_info, teacher
