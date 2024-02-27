import re

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from core.common.constants import CHECK_VALUES


@dataclass
class BaseLessonParser(ABC):
    teacher_ranks: CHECK_VALUES.TEACHERS_RANKS = field(default=CHECK_VALUES.TEACHERS_RANKS.value)

    @abstractmethod
    def parse_string(self, string: str):
        ...


class LessonParserService(BaseLessonParser):
    def parse_string(self, string: str):
        if "/" not in string and "+" not in string:
            lesson_teacher_dict = self.parse_string_without_additions(string=string)
            return lesson_teacher_dict
        if "/" in string:
            return self.parse_slash_string(string=string)
        if "+" in string:
            return self.parse_plus_string(string=string)

    def parse_string_without_additions(self, string: str):

        rank_pattern = '|'.join(re.escape(rank) for rank in self.teacher_ranks)
        matches = re.finditer(rank_pattern, string)

        indexes = [match.start() for match in matches]

        divider = min(indexes) if indexes else len(string)

        lesson = string[:divider].strip(" ")
        teacher = string[divider:].strip(" ")

        if "," in teacher:
            teachers = re.split(r',(?![^(]*\))', teacher)
            return {"Lesson": lesson,
                    "Teacher": [teacher.strip() for teacher in teachers]}
        return {"Lesson": lesson,
                "Teacher": teacher}

    def parse_slash_string(self, string: str):
        string_list = string.split('/')

        lessons = []
        teachers = []

        for string in string_list:
            lesson_teacher_dict = self.parse_string_without_additions(string=string)


