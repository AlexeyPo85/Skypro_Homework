import requests
import os
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(code: str, amount: str) -> float:
    " Функция конвертирует сумму в RUB по текущему курсу."

    if code != "USD" or code != "EUR" or float(amount) != float:
        return {}
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        headers = {"apikey": os.getenv("API_KEY")}
        payload = {}
        response = requests.get(url, headers=headers, data = payload)
        status_code = response.status_code
        result = response.json()
        result_amount = result["result"]
        return result_amount

print(convert_to_rub("USD", "a"))
