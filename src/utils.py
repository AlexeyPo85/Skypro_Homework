import json
import os.path

from src.external_api import convert_to_rub


def get_list_transactions(json_file) -> list:
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


def get_amount_rub(transaction: dict) -> float:
    """ Функция принимает данные транзакции и возвращает сумму транзакции в рублях.
    Если транзакция в USD или EUR, происходит конвертация в RUB по текущему курсу."""

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        return convert_to_rub(transaction["operationAmount"]["currency"]["code"],
                              transaction["operationAmount"]["amount"])
