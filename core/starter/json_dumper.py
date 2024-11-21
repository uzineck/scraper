import json
import os


class JsonDumper:
    @staticmethod
    def dump(dict_data: dict, filename: str, dir_name: str):
        directory_path = f"D:/pythonwork/ExcelScraper_2.0/json_schedules/{dir_name}/"

        directory = os.path.dirname(directory_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = f"{directory_path}{filename}.json"
        with open(filepath, 'w', encoding='utf8') as f:
            json.dump(dict_data, f, indent=4, ensure_ascii=False)
