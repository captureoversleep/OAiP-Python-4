def calc_total(count):
    total = 0
    for i in range(count):
        score = int(input("Введите балл за предмет: "))
        total = total + score
    return total

def reward(total_score):
    print("Итоговый счёт:", total_score)
    if total_score > 80:
        print("Наградить дипломом.")
    elif total_score > 50:
        print("Наградить похвальной грамотой.")
    else:
        print("Выдать грамоту об участии.")





name = input("Введите имя студента: ")
subj_count = int(input("Введите число предметов: "))

final_score = calc_total(subj_count)
reward(final_score)