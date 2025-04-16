from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(user_account: str) -> str:
    """ Функция принимает номер карты или счет и возвращает в замаскированном виде"""

    splited_user_account = user_account.split()
    if splited_user_account[0] == "Счет":
        return get_mask_account(splited_user_account[1])
    else:
        return get_mask_card_number(splited_user_account[-1])

