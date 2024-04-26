#Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів,
# що містить лише літери та цифри.
import re


def validate_login(login):
    pattern = r'^[A-Za-z0-9]\w{2,10}$'

    if re.match(pattern, login):
        return True
    else:
        return False


login = "Useм123"
is_valid = validate_login(login)
print(f"The login '{login}' is {'valid' if is_valid else 'invalid'}.")
