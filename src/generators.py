def filter_by_currency(transact: list[dict], code: str) -> iter:
    """ Функция принимает список словарей транзакций и возвращает
    итератор, который поочередно выдает транзакции по заданной валюте."""

    if transact == [{}]:
        yield "Отсутствует список транзакций"
    if code == "":
        yield "Не задана искомая валюта"
    if code == "USD" or code == "RUB":
        for action in transact:
            if action["operationAmount"]["currency"]["code"] == code:
                yield action
    yield "Транзакции в заданной валюте не найдены"


def transaction_descriptions(transact: list[dict]) -> iter:
    """ Функция возвращает описание каждой операции из списка словарей с транзакциями."""

    if transact == [{}]:
        yield "Отсутствует список транзакций"
    for operation in transact:
        descript = operation["description"]
        yield descript


def card_number_generator(start: int, stop: int) -> iter:
    """ Функция генерирует номера карт от 0000 0000 0000 0000 до 9999 9999 9999 9999
    по заданному диапазону."""

    if isinstance(start, int) and isinstance(stop, int):
        if start < 0 or stop < 0:
            yield "Введён неверный диапазон"
        zero_number = '0000000000000000'
        for num in range(start, stop + 1):
            if num <= 9999999999999999:
                result_num = zero_number[: -len(str(num))] + str(num)
                yield f'{result_num[: 4]} {result_num[4: 8]} {result_num[8: 12]} {result_num[12:]}'
            else:
                yield "Превышено количество знаков в номере карты"
    else:
        yield "Введён неверный диапазон"
