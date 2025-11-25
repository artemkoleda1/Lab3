# Задание A2: Проверка надежности пароля

import string

password = input()

# Список для хранения ошибок
errors = []

# длины
if len(password) != 8:
    errors.append("Длина пароля не равна 8")

# заглавные
if password == password.lower():
    errors.append("В пароле отсутствуют заглавные буквы")

# строчные
if password == password.upper():
    errors.append("В пароле отсутствуют строчные буквы")

# цифры
if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")

# спец символы
special_chars = '*-#'
if not any(symbol in special_chars for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")

# недопустимые символы
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
if not all(symbol in allowed for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")

# вывод
if len(errors) == 0:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)
