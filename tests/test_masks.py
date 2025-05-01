import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


@pytest.mark.parametrize('card_num, result', [('1596837868705199', '1596 83** **** 5199'),
                                              ('0000000000000000', '0000 00** **** 0000'),
                                              ('1', 'Введён не корректный номер карты'),
                                              ('abcdefghijklmnop', 'Введён не корректный номер карты'),
                                              ('ccc', 'Введён не корректный номер карты'),
                                              ([1, 2, 3], 'Введён не корректный номер карты'),
                                              ])
def test_get_mask_card_number_2(card_num, result):
    assert get_mask_card_number(card_num) == result


def test_get_mask_card_number_3():
    assert get_mask_card_number('') == 'Введён не корректный номер карты'


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == '**4305'


@pytest.mark.parametrize('account_num, result', [('64686473678894779589', '**9589'),
                                                 ('00000000000000000000', '**0000'),
                                                 ('123', 'Введён не корректный номер счёта'),
                                                 ('abcdefghijklmnopqrst', 'Введён не корректный номер счёта'),
                                                 ('abc', 'Введён не корректный номер счёта'),
                                                 ('', 'Введён не корректный номер счёта'),
                                                 ([1, 2, 3], 'Введён не корректный номер счёта'),
                                                 ])
def test_get_mask_account_2(account_num, result):
    assert get_mask_account(account_num) == result