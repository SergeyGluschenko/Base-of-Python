from functools import reduce
from typing import List


def my_func(num1, num2):
    return float(num1) + float(num2)


user_num = input('Введите числа разделенные пробелом и получите их сумму: ')

with open('text_5_5.txt', 'w', encoding='utf-8') as file:
    file.write(user_num)  # записали в файл числа для подсчета


'''можно на прямую подсчитать введинные числа, но тогда не потренируем
работу с файлами'''

with open('text_5_5.txt', 'r', encoding='utf-8') as file:
    list_num = (file.readline()).split()


print(f"Сумма ваших цифр -> {reduce(my_func, list_num)}")


