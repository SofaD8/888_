#Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
import re


def validate_credit_card(card_number):
    pattern = r'^[0-9]{4}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$'

    if re.match(pattern, card_number):
        return True
    else:
        return False


card_number = "9999-9999-9999-9999"
is_valid = validate_credit_card(card_number)
print(f"The card number {card_number} is {'valid' if is_valid else 'invalid'}.")
