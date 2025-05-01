import pytest
from packaging.licenses import EXCEPTIONS

from src.masks import get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'
    assert get_mask_card_number('1596837868705199') == '1596 83** **** 5199'
    assert get_mask_card_number('0000000000000000') == '0000 00** **** 0000'

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('1')
        assert str(exc_info.value) == 'Введён не корректный номер карты'

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('')
        assert str(exc_info.value) == 'Введён не корректный номер карты'

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('abcdefghijklmnop')
        assert str(exc_info.value) == 'Введён не корректный номер карты'
