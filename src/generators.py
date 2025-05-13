def filter_by_currency(transact: list[dict], code: str) -> iter:
    """ Функция принимает список словарей транзакций и возвращает
    итератор, который поочередно выдает транзакции по заданной валюте."""

    for action in transact:
        if action["operationAmount"]["currency"]["code"] == code:
            yield action


def transaction_descriptions(transact: list[dict]) -> iter:
    """ Функция возвращает описание каждой операции из списка словарей с транзакциями."""

    for operation in transact:
        descript = operation["description"]
        yield descript


def card_number_generator(start: int, stop: int) -> iter:
    """ Функция генерирует номера карт от 0000 0000 0000 0000 до 9999 9999 9999 9999
    по заданному диапазону."""

    zero_number = '0000000000000000'
    for num in range(start, stop + 1):
        result_num = zero_number[: -len(str(num))] + str(num)
        yield f'{result_num[: 4]} {result_num[4: 8]} {result_num[8: 12]} {result_num[12:]}'
