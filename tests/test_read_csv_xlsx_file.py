from unittest.mock import patch

import pandas as pd

from src.read_csv_xlsx_file import read_csv_file, read_xlsx_file


@patch("src.read_csv_xlsx_file.pd.read_csv")
def test_read_csv_file(mocked_get):
    df = pd.DataFrame({"city": ["Piter", "Moscow"], "age": ["2001", "1999"]})
    mocked_get.return_value = df
    result = read_csv_file("transactions.csv")
    assert result == [{'city': 'Piter', 'age': '2001'}, {'city': 'Moscow', 'age': '1999'}]


def test_read_csv_file_2():
    assert read_csv_file("none.csv") == []


@patch("src.read_csv_xlsx_file.pd.read_excel")
def test_read_xlsx_file(mocked_get):
    df = pd.DataFrame({"city": ["Piter", "Moscow"], "age": ["2001", "1999"]})
    mocked_get.return_value = df
    result = read_xlsx_file("transactions.csv")
    assert result == [{'city': 'Piter', 'age': '2001'}, {'city': 'Moscow', 'age': '1999'}]


def test_read_xlsx_file_2():
    assert read_xlsx_file("none.xlsx") == []
