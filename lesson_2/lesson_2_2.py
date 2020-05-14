user_list = []
number_items = int(input("Введите количество элементов в списке: "))
count = 0
while count < number_items:
    user_list.append(input(f'Осталось ввести элементов списка'
                           f' {number_items-count}. Введите элемент спискa: '))
    count +=1

print(user_list) # выводим полученный от пользователя список

if number_items > 1:
    even = 0
    not_even = 1
    i = 0
    while i < number_items // 2:
        user_list[even], user_list[not_even] =\
            user_list[not_even], user_list[even]
        i += 1
        even += 2
        not_even += 2

print(user_list) # выводим полученный список после сортировки
