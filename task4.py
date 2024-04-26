import re


# Функція для валідації логіну
def validate_login(login):
    # Регулярний вираз для перевірки логіну
    pattern = r'^[A-Za-z0-9]{2,10}$'

    # Перевірка логіну за допомогою регулярного виразу
    if re.match(pattern, login):
        return True
    else:
        return False


# Приклад використання
login = "User123"
is_valid = validate_login(login)
print(f"The login '{login}' is {'valid' if is_valid else 'invalid'}.")