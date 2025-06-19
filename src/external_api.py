import logging

import requests
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("external_api")
file_handler = logging.FileHandler("../logs/external_api.log","w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def convert_to_rub(code: str, amount: str) -> float:
    """ Функция конвертирует сумму в RUB по текущему курсу."""

    logger.info("Начало работы функции convert_to_rub")
    try:
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}'
        headers = {"apikey": os.getenv("API_KEY")}
        payload: dict = {}
        logger.info("Функция отправляет запрос на конвертацию")
        response = requests.get(url, headers=headers, data=payload)
        logger.info("Функция получает ответ")
        status_code = response.status_code
        result = response.json()
        result_amount = result["result"]
        logger.info("Функция возвращает сумму транзакции в RUB")
        return result_amount
    except Exception:
        logger.warning("Ошибка. Что-то пошло не так")
        return float
