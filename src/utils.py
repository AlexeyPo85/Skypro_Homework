import json
import os.path


def get_list_transactions(json_file: json) -> list[dict]:
    " Функция принимает файл формата json, и возвращает список транзакций."

    path_func = os.path.abspath(__file__)
    path_file = os.path.join(path_func, "..", "..", "data", json_file)
    with open(path_file, encoding="utf-8") as f:
        try:
            result = json.load(f)
            if type(result) != list:
                return []
            return result
        except json.JSONDecodeError:
            return []



