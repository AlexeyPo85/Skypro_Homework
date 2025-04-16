from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(user_account: str) -> str:
    """ Функция принимает номер карты или счет и возвращает в замаскированном виде"""

    splited_user_account = user_account.split()
    if splited_user_account[0] == "Счет":
        return get_mask_account(splited_user_account[1])
    else:
        return get_mask_card_number(splited_user_account[-1])


def get_date(date_and_info: str) -> str:
    info_splited = date_and_info.split("T")
    date_splited = info_splited[0].split("-")
    date = f"{date_splited[2]}.{date_splited[1]}.{date_splited[0]}"
    return date
