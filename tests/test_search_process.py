from unicodedata import category

from src.search_process import process_bank_search, process_bank_operations


def test_process_bank_search(list_of_transactions):
    result = [  {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }]
    assert process_bank_search(list_of_transactions, "Перевод с карты на карту") == result


def test_process_bank_search_2():
    operations_list = []
    assert process_bank_search(operations_list, "Перевод с карты на карту") == []


def test_process_bank_search_3(list_of_transactions):
    operation = ""
    assert process_bank_search(list_of_transactions, operation) == []


def test_process_bank_operations(list_of_transactions):
    categories = ["Перевод организации", "Перевод с карты на карту"]
    result = {"Перевод организации": 2, "Перевод с карты на карту": 1}
    assert process_bank_operations(list_of_transactions, categories) == result

def test_process_bank_operations_2():
    data = []
    categories = ["Перевод организации", "Перевод с карты на карту"]
    assert process_bank_operations(data, categories) == {}


def test_process_bank_operations_3(list_of_transactions):
    categories = []
    assert process_bank_operations(list_of_transactions,categories) == {}
