from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_account: str) -> str:
    """ Функция принимает номер карты или счета и возвращает в замаскированном виде"""

    if not user_account:
        return 'Введёно не корректное значение'

    if not isinstance(user_account, str):
        return 'Введёно не корректное значение'

    splited_user_account = user_account.split()
    if splited_user_account[0] == 'Счет':
        return get_mask_account(splited_user_account[-1])
    else:
        return get_mask_card_number(splited_user_account[-1])


def get_date(date_and_info: str) -> str:
    """ Функция возвращает дату в формате ДД.ММ.ГГГГ"""

    if not isinstance(date_and_info, str):
        return 'Введено не корректное значение даты'

    info_splited = date_and_info.split('T')

    if not info_splited[0]:
        return 'Введено не корректное значение даты'

    if info_splited[0].count('-') != 2:
        return 'Введено не корректное значение даты'

    date_splited = info_splited[0].split('-')

    if not date_splited[0] or not date_splited[1] or not date_splited[2]:
        return 'Введено не корректное значение даты'

    if not 0 < int(date_splited[2]) < 31 or not 0 < int(date_splited[1]) < 13 or not 0 < int(date_splited[0]) < 2025:
        return 'Введено не корректное значение даты'
    # Библиотеки ещё не изучали, поэтому принял что в месяце 30 дней

    date = f'{date_splited[2]}.{date_splited[1]}.{date_splited[0]}'
    return date
