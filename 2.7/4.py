def define_place(score):
    if score >= 50 and score < 65:
        place = '3 место'
    elif score >= 65 and score < 85:
        place = '2 место'
    elif score >= 85:
        place = '1 место'
    else:
        place = 'Повезет в другой раз!'
    return place

score = int(input('Введите количество очков: '))
place = define_place(score)
print(place)