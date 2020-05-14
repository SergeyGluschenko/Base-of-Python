my_list = [7, 5, 3, 3, 2]
while True:
    try: # пользователь должен ввести именно число
        user_num = int(input('Введите элемент(число) рейтинга: '))
        if type(user_num) == int:
            break
    except ValueError:
        print('Введено не число!')

count = 0 # счетчик номера элемента в рейтинге
for i in my_list:
    if user_num > i:
        my_list.insert(count, user_num)
        break
    count +=1
    if user_num < my_list[-1]:
        my_list.append(user_num)
print(my_list)
