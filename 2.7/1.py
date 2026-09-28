def self_checkout():
    while True:
        cat = input('Введите категорию: ')
        if cat == 'off':
            print('Касса закрыта')
            break
        elif cat.lower() == 'молочные продукты':
            discount = 10
        elif cat.lower() == 'выпечка':
            discount = 30
        else:
            print('Скидок нет :(')
            discount = 0
        price = float(input('Введите цену товара: '))

        if discount > 0:
            price = price - (price / 100 * discount)
            print('Цена за товар cо скидкой:', price)
        else:
            print('Цена за товар:', price)           
print('Добро пожаловать в кассу самообслуживания')
self_checkout()
