from src.external_api import convert_to_rub
from unittest.mock import patch


@patch("src.external_api.requests.get")
def test_convert_to_rub(mocked_get):
    mocked_get.return_value.json.return_value = {'result': 123.001}
    result = convert_to_rub("USD", "1.001")
    assert result == 123.001


@patch("src.external_api.requests.get")
def test_convert_to_rub_negative_args(mocked_get):
    mocked_get.return_value.json.return_value = {}
    result = convert_to_rub("a4", "a")
    assert result == float
