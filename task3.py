import re


# Функція для валідації електронної адреси
def validate_email(email):
    # Регулярний вираз для перевірки електронної адреси
    pattern = r'^(?![_-])[A-Za-z0-9]+(?:[._-]?[A-Za-z0-9]+)*@[A-Za-z0-9-]+(?:\\.[A-Z|a-z]{2,})+$'

    # Перевірка електронної адреси за допомогою регулярного виразу
    if re.match(pattern, email):
        return True
    else:
        return False


# Приклад використання
email = "example_email@example.com"
is_valid = validate_email(email)
print(f"Електронна адреса {email} є {'валідною' if is_valid else 'невалідною'}.")