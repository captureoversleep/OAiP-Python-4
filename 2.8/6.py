def check_name(name):
    if name != "" and len(name) < 50:
        return True
    return False

def check_age(age):
    if age >= 18 and age <= 120:
        return True
    return False

def check_email(email):
    if "@" in email:
        return True
    return False

def validate_user(name, age, email):
    if check_name(name) and check_age(age) and check_email(email):
        return True
    return False

name = input('Введите логин: ')
age = int(input('Введите возраст: '))
email = input('Введите email: ')
result = validate_user(name, age, email)
print(result)