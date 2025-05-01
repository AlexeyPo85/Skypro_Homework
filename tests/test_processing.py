import pytest

from src.processing import filter_by_state


def test_filter_by_state(dicts):
    assert filter_by_state(dicts) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_filter_by_state_2(dicts):
    assert filter_by_state(dicts, 'CANCELED') == [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.mark.parametrize('input_dicts, states, result', [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                        {'id': 594226727, 'state': 'NOT FOUND', 'date': '2018-09-12T21:27:25.241689'},
                                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                                          'NOT FOUND',
                                                          [{'id': 594226727, 'state': 'NOT FOUND', 'date': '2018-09-12T21:27:25.241689'}]),
                                                         ])
def test_filter_by_state_3(input_dicts, states, result):
    assert filter_by_state(input_dicts, states) == result


def test_filter_by_state_4(dicts_no_state_value):
    assert filter_by_state(dicts_no_state_value) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_filter_by_state_5(dicts):
    assert filter_by_state(dicts, 'NOT FOUND') == []


def test_filter_by_state_6(dicts_no_state):
    with pytest.raises(KeyError):
        filter_by_state(dicts_no_state)


def test_filter_by_state_7(dicts_no_type_str):
    assert filter_by_state(dicts_no_type_str) == []
