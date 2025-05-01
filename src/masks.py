def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карты, видны первые 6 и последние 4 цифры"""

    if len(card_number) != 16:
        raise ValueError('Введён не корректный номер карты')

    if card_number.isdigit() == False:
        raise ValueError('Введён не корректный номер карты')

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция возвращает маску номера счета в которй видны последние 4 цифры"""

    return f"**{account[-4:]}"
