import pytest

from src.widget import mask_account_card


def test_mask_account_card(name_card_number):
    assert mask_account_card(name_card_number) == '7000 79** **** 6361'


def test_mask_account_card_2(name_account_number):
    assert mask_account_card(name_account_number) == '**4305'


@pytest.mark.parametrize('input_data, result', [('Maestro 1596837868705199', '1596 83** **** 5199'),
                                                ('Счет 64686473678894779589', '**9589'),
                                                ('Visa Classic 0000000000000000', '0000 00** **** 0000'),
                                                ('Maestro ', 'Введён не корректный номер карты'),
                                                ('', 'Введёно не корректное значение'),
                                                ('Счет ', 'Введён не корректный номер счёта'),
                                                ('Счет', 'Введён не корректный номер счёта'),
                                                ('Счет 123', 'Введён не корректный номер счёта'),
                                                ('123', 'Введён не корректный номер карты'),
                                                ('64686473678894779589', 'Введён не корректный номер карты'),
                                                ([1,2,3], 'Введёно не корректное значение'),
                                                ])
def test_mask_account_card_3(input_data, result):
    assert mask_account_card(input_data) == result
