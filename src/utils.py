import json
import logging
import os.path

from src.external_api import convert_to_rub

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_list_transactions(json_file) -> list:
    """ Функция принимает файл формата json, и возвращает список транзакций."""

    logger.info("Начало работы функции  get_list_transactions")
    path_func = os.path.abspath(__file__)
    path_file = os.path.join(path_func, "..", "..", "data", json_file)
    try:
        logger.info("Функция открывает указанный файл")
        with open(path_file, encoding="utf-8") as f:
            try:
                result = json.load(f)
                if type(result) is not list:
                    logger.error("Данные в файле не являются списком")
                    return []
                logger.info("Функция возвращает результат")
                return result
            except json.JSONDecodeError:
                logger.error("Ошибка файла")
                return []
    except FileNotFoundError:
        logger.error("Ошибка. Файл не найден")
        return []


def get_amount_rub(transaction: dict) -> float:
    """ Функция принимает данные транзакции и возвращает сумму транзакции в рублях.
    Если транзакция в USD или EUR, происходит конвертация в RUB по текущему курсу."""

    logger.info("Начало работы функции get_amount_rub")
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("Функция возвращает сумму транзакции если транзакция в RUB")
        return float(transaction["operationAmount"]["amount"])
    else:
        logger.info("Функция передает запрос функции convert_to_rub если транзакция в USD или EUR")
        return convert_to_rub(transaction["operationAmount"]["currency"]["code"],
                              transaction["operationAmount"]["amount"])
