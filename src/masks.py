def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карты, видны первые 6 и последние 4 цифры"""

    if len(card_number) != 16:
        return 'Введён не корректный номер карты'

    if card_number.isdigit() == False:
        return 'Введён не корректный номер карты'

    if isinstance(card_number, str) == False:
        return 'Введён не корректный номер карты'

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция возвращает маску номера счета в которой видны последние 4 цифры"""

    if len(account) != 20:
        return 'Введён не корректный номер счёта'

    if account.isdigit() == False:
        return 'Введён не корректный номер счёта'

    if isinstance(account, str) == False:
        return 'Введён не корректный номер счёта'

    return f"**{account[-4:]}"
