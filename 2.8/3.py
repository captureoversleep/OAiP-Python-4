def get_score():
    for i in range(3):
        score = int(input('Введите балл:'))
        if score >= 65 and score <= 100:
            print('Успеваемость в норме')
        elif score < 65:
            print('Низкая успеваемость!')
        else:
            print('Некорректный ввод')
    

get_score()
