import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карты, видны первые 6 и последние 4 цифры"""

    logger.info("Начало работы функции  get_mask_card_number")
    if len(card_number) != 16:
        logger.error('Введён не корректный номер карты')
        return 'Введён не корректный номер карты'

    if not card_number.isdigit():
        logger.error('Введён не корректный номер карты')
        return 'Введён не корректный номер карты'

    if not isinstance(card_number, str):
        logger.error('Введён не корректный номер карты')
        return 'Введён не корректный номер карты'

    logger.info("Вывод маски номера карты")
    return f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'


def get_mask_account(account: str) -> str:
    """Функция возвращает маску номера счета в которой видны последние 4 цифры"""

    logger.info("Начало работы функции  get_mask_account")
    if len(account) != 20:
        logger.error('Введён не корректный номер счёта')
        return 'Введён не корректный номер счёта'

    if not account.isdigit():
        logger.error('Введён не корректный номер счёта')
        return 'Введён не корректный номер счёта'

    if not isinstance(account, str):
        logger.error('Введён не корректный номер счёта')
        return 'Введён не корректный номер счёта'

    logger.info("Вывод маски номера счёта")
    return f'**{account[-4:]}'
