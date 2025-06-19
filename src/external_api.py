import logging

import requests
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("external_api")


def convert_to_rub(code: str, amount: str) -> float:
    """ Функция конвертирует сумму в RUB по текущему курсу."""

    try:
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}'
        headers = {"apikey": os.getenv("API_KEY")}
        payload: dict = {}
        response = requests.get(url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        result_amount = result["result"]
        return result_amount
    except Exception:
        return float


print(convert_to_rub("USD", ""))
