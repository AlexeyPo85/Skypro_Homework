from src.generators import filter_by_currency, transaction_descriptions
from tests.conftest import list_of_transactions


def test_filter_by_currency_1(list_of_transactions, for_filter_by_currency_1, for_filter_by_currency_2):
    result = filter_by_currency(list_of_transactions, "USD")
    assert next(result) == for_filter_by_currency_1
    assert next(result) == for_filter_by_currency_2


def test_filter_by_currency_2(list_of_transactions, for_filter_by_currency_3):
    result = filter_by_currency(list_of_transactions, "RUB")
    assert next(result) == for_filter_by_currency_3


def test_filter_by_currency_3():
    result = filter_by_currency([{}], "USD")
    assert next(result) == "Отсутствует список транзакций"


def test_filter_by_currency_4(list_of_transactions):
    result = filter_by_currency(list_of_transactions, "")
    assert next(result) == "Не задана искомая валюта"


def test_filter_by_currency_5(list_of_transactions,):
    result = filter_by_currency(list_of_transactions, "EUR")
    assert next(result) == "Транзакции в заданной валюте не найдены"


def test_transaction_descriptions_1(list_of_transactions):
    result = transaction_descriptions(list_of_transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод с карты на карту"


def test_transaction_descriptions_2():
    result = transaction_descriptions([{}])
    assert next(result) == "Отсутствует список транзакций"


def test_transaction_descriptions_3(list_of_transactions_2):
    result = transaction_descriptions(list_of_transactions_2)
    assert next(result) == "Перевод организации"
    assert next(result) == ""
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == ""
    assert next(result) == "Перевод организации"
