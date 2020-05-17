def def_sum(list_def):
    sum_list = sum(list_def)
    print(f'Сумма строки равна: {sum_list}')
    return sum_list


sum_num = 0
while True:
    list_user = input('Введи строку цифр, разделенных пробелом.'
                      ' Для завершения программы введите "Q": ').split(' ')
    if list_user.count('Q') > 0:
        # Нахадим под каким индексом в списке 'Q'
        # и берем список от начала до этого индекса
        list_user = list(map(int, list_user [:list_user.index('Q')]))
        sum_num += def_sum(list_user)
        print(f'Сумма всех строк равна: {sum_num}')
        break
    list_user = list(map(int, list_user))
    sum_num += def_sum(list_user)
    print(f'Сумма всех строк равна: {sum_num}')

print('Работа программы завершена')