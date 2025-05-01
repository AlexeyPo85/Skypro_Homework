import pytest

from src.masks import get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


@pytest.mark.parametrize('card_num, result', [('1596837868705199', '1596 83** **** 5199'),
                                              ('0000000000000000', '0000 00** **** 0000'),
                                              ('1', 'Введён не корректный номер карты'),
                                              ('abcdefghijklmnop', 'Введён не корректный номер карты'),
                                              ('ccc', 'Введён не корректный номер карты'),
                                              ])
def test_get_mask_card_number_2(card_num, result):
    assert get_mask_card_number(card_num) == result


def test_get_mask_card_number_3():
    assert get_mask_card_number('') == 'Введён не корректный номер карты'


