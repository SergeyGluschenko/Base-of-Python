def divide_num(def_num1, def_num2):
    try:
        print(def_num1 /def_num2)
    except ZeroDivisionError:
        print('Деление на ноль! Следующий раз, ноль не вводете')

# из условии не ясно, в функции или в программе запрашиать цифры у пользователя
user_name1 = int(input('Введите первое число: '))
user_name2 = int(input('Введите второе число: '))
divide_num(user_name1, user_name2)