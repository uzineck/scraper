import json


class JsonDumper:
    @staticmethod
    def dump(dict_data: dict, filename: str):
        filepath = f"D:\pythonwork\ExcelScraper_2.0\json_schedules\{filename}.json"
        with open(filepath, 'w', encoding='utf8') as f:
            json.dump(dict_data, f, indent=4, ensure_ascii=False)
