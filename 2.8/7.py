def analyze(amount):
    if amount <= 8000:
        print('Сумма ниже среднего.')
    elif amount < 10000:
        print('Оптимальная сумма.')
    else:
        print('Необходимо согласование!')

def calc_budg():
    total = 0
    while True:
        amount = int(input('Введите сумму расхода (0 для выхода): '))
        if amount <= 0:
            break
        analyze(amount)
        total = total + amount
    print('Всего запрошено денег:', total)

calc_budg()