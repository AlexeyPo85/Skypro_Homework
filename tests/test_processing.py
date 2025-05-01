import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(dicts, dicts_result_1):
    assert filter_by_state(dicts) == dicts_result_1


def test_filter_by_state_2(dicts, dicts_result_2):
    assert filter_by_state(dicts, 'CANCELED') == dicts_result_2


def test_filter_by_random_state(dicts_random_state, dicts_random_state_result):
    assert filter_by_state(dicts_random_state, 'NOT FOUND') == dicts_random_state_result


def test_filter_by_state_4(dicts_no_state_value):
    assert filter_by_state(dicts_no_state_value) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]


def test_filter_by_state_5(dicts):
    assert filter_by_state(dicts, 'NOT FOUND') == []


def test_filter_by_state_6(dicts_no_state):
    with pytest.raises(KeyError):
        filter_by_state(dicts_no_state)


def test_filter_by_state_7(dicts_no_type_str):
    assert filter_by_state(dicts_no_type_str) == []


def test_sort_by_date_true(dicts_to_data, sorted_dicts_true):
    assert sort_by_date(dicts_to_data) == sorted_dicts_true


def test_sort_by_date_false(dicts_to_data, sorted_dicts_false):
    assert sort_by_date(dicts_to_data, False) == sorted_dicts_false


def test_sort_by_date_no_data_value(dicts_no_data_value, dicts_no_data_value_result):
    assert sort_by_date(dicts_no_data_value) == dicts_no_data_value_result


def test_sort_by_date_no_data(dicts_no_data, dicts_no_data_result):
    assert sort_by_date(dicts_no_data) == dicts_no_data_result
