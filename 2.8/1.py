def get_marks():
    five_count = 0
    while True:
        mark=int(input('Введите оценку (0 - выход): '))
        if mark == 5:
            five_count += 1
        elif mark == 0:
            break
    return five_count

def get_discount(five_count):
    discount = '0%'
    if five_count == 4 or five_count == 5:
        discount = '10%'
    elif five_count > 5:
        discount = '15%'
    return discount

five_count = get_marks()
discount = get_discount(five_count)
if discount != '0%':
    print('Скидка на билеты в театр:', discount)
else:
    print('Скидок нет!')