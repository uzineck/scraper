import json


def load_json(filepath: str) -> dict:
    with open(filepath, 'r', encoding='UTF-8') as file:
        return json.load(file)


def dump_set(_set: set, filename: str) -> None:
    with open(f'../../items/{filename}.json', 'w', encoding='UTF-8') as file:
        json.dump(list(_set), file, ensure_ascii=False, indent=4)
