from src.utils import get_list_transactions, get_amount_rub
from unittest.mock import patch


@patch("src.utils.json.load")
def test_get_list_transactions(mocked_get):
    mocked_get.return_value = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"}
        }
    },]
    result = get_list_transactions("operations.json")
    assert result == [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"}
        }
    },]


@patch("src.utils.json.load")
def test_get_list_transactions_2(mocked_get):
    mocked_get.return_value = []
    result = get_list_transactions("operations.json")
    assert result == []


@patch("src.utils.json.load")
def test_get_list_transactions_3(mocked_get):
    mocked_get.return_value = '[1, 2, "a", "b"]'
    result = get_list_transactions("operations.json")
    assert result == []


@patch("src.utils.json.load")
def test_get_list_transactions_4(mocked_get):
    mocked_get.return_value = None
    result = get_list_transactions("operations.json")
    assert result == []


def test_get_amount_rub(list_of_transactions_for_utils):
    result = get_amount_rub(list_of_transactions_for_utils)
    assert result == 31957.58


@patch("src.utils.convert_to_rub")
def test_get_amount_rub_2(mocked_get, list_of_transactions_for_utils_2):
    mocked_get.return_value = 100.001
    result = get_amount_rub(list_of_transactions_for_utils_2)
    assert result == 100.001
