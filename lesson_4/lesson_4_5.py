from functools import reduce


def my_func(num1, num2):
    return num1 * num2


# start_num = int(input('Введите начало диапазона: '))
start_num = 100
# finish_num = int(input('Введите конец диапазона: '))
finish_num = 1000
new_list = [el for el in range(start_num, finish_num + 1) if el % 2 == 0]
print(new_list)
print(reduce(my_func, new_list))