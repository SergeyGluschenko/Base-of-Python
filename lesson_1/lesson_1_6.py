start_result = int(input("Введите начальный результат спортсмена: "))
finish_result = int(input("Введите конечную цель спортсмена: "))
number_day = 1
level = start_result
while level < finish_result:
    level = round(1.1 * level, 2)  # увеличиваем результат на 10%
    number_day += 1
print(f'Ответ: на {number_day}-й день спортсмен достиг результата — не менее {finish_result} км.')
