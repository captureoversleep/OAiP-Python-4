def calc_bmi(weight, height): #вес в кг, рост в м
    index = weight / (height * height)
    return index

def print_recomendation(weight, height):
    index = calc_bmi(weight, height)
    if index <= 18.5:
        print('У вас недостаточный вес, пройдите на консультацию в кабинет 301')
    if index > 18.5 and index <= 25:
        print('Ваш вес в норме, пройдите на 3 этаж для продолжения осмотра')
    if index > 25:
        print('У вас избыточный вес, пройдите на консультацию в кабинет 410')



weight = float(input('Введите вес (кг):'))
height = float(input('Введите рост (м):'))
print_recomendation(weight, height)
