#Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
#Вимоги:
#-Цифри (0-9).
#-лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
#-у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
#-Символ "-" не може повторюватися.
import re


def is_valid_email(email):
    regex = r"^(?![_-])[A-Za-z0-9._-]+(?<![-])@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.match(regex, email):
        if "--" not in email.split('@')[0]:
            return True
    return False


test_emails = ["example_email@example.com", "_example@example.com", "example--email@example.com",
               "example-email@example.com", "example-email@example.io.com"]
for email in test_emails:
    print(f"Is '{email}' a valid email? {is_valid_email(email)}")
