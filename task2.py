import re


# Define a function to validate a credit card number
def validate_credit_card(card_number):
    # Define the regular expression pattern for a credit card number
    pattern = r'^\\d{4}-\\d{4}-\\d{4}-\\d{4}$'

    # Use the regular expression to match the card number
    if re.match(pattern, card_number):
        return True
    else:
        return False


# Example usage
card_number = "9999-9999-9999-9999"
is_valid = validate_credit_card(card_number)
print(f"The card number {card_number} is {'valid' if is_valid else 'invalid'}.")