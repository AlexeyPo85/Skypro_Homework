from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

user_input = "Maestro 1596837868705199"
user_input_2 = "Счет 35383033474447895560"
user_input_3 = "Visa Platinum 8990922113665229"

print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
print()
print(mask_account_card(user_input))
print(mask_account_card(user_input_2))
print(mask_account_card(user_input_3))

