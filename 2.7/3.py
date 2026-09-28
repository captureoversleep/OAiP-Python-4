def login_check(login):
    restricted = ('=?*^$№@_')
    for symbol in login:
        if symbol in restricted:
            print(symbol)

login = input('Введите логин: ')
login_check(login)