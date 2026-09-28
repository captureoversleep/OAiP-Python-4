def define_place(score):
    if score >= 50 and score < 65:
        place = '3 место'
    elif score >= 65 and score < 85:
        place = '2 место'
    elif score >= 85:
        place = '1 место'
    else:
        place = 'участник'
    return place

def define_prize(place):
    if place == '1 место':
        prize = 'Поездка в Санкт-Петербург'
    elif place == '2 место':
        prize = 'Сертификат в книжный магазин'
    elif place == '3 место':
        prize = 'Настольная игра'
    else:
        prize = 'Сертификат участника'
    print(prize)

score = int(input('Введите количество очков: '))
place = define_place(score)
define_prize(place)