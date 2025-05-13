import pytest

from src.widget import get_date, mask_account_card


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
                                                ([1, 2, 3], 'Введёно не корректное значение'),
                                                ])
def test_mask_account_card_3(input_data, result):
    assert mask_account_card(input_data) == result


def test_get_date(date_in_data):
    assert get_date(date_in_data) == '11.03.2024'


@pytest.mark.parametrize('input_data, result', [('1988-03-60T02:26:18.671407', 'Введено не корректное значение даты'),
                                                ('3000-01-01T02:26:18.671407', 'Введено не корректное значение даты'),
                                                ('30-01-2001T02:26:18.671407', 'Введено не корректное значение даты'),
                                                ('T02:26:18.671407', 'Введено не корректное значение даты'),
                                                ('12-2024T02:26:18.671407', 'Введено не корректное значение даты'),
                                                ('2024T02:26:18.671407', 'Введено не корректное значение даты'),
                                                ([1, 2, 3], 'Введено не корректное значение даты'),
                                                ('2000-05-05T02:26:18.671407', '05.05.2000'),
                                                ('1674-12-25T02:26:18.671407', '25.12.1674'),
                                                ])
def test_get_date_2(input_data, result):
    assert get_date(input_data) == result
