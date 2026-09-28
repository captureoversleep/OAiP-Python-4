def show_lab_info():
    print('Лаборатория находится на третьем этаже в кабинете A-302')
    print('Там проходят практические занятия и научные эксперименты')

def show_lec_info():
    print('Лекторий расположен на первом этаже, зал A-101')
    print('Здесь вы можете послушать лекции ведущих ученых и экспертов.')

def start_nav():
    while True:
        u_choice = input('Что вас интересует (стоп - завершить): ')
        u_choice = u_choice.lower()
        
        if u_choice == 'стоп':
            break
        elif u_choice == 'лаборатория':
            show_lab_info()
        elif u_choice == 'лекторий':
            show_lec_info()
        else:
            print('Некорректный ввод')

start_nav()