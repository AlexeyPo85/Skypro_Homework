import requests
import os
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(code: str, amount: str) -> float:
    " Функция конвертирует сумму в RUB по текущему курсу."

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}
    payload = {}
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    result = response.json()
    result_amount = result["result"]
    return result_amount
