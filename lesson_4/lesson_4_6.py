from sys import argv
from itertools import count, cycle


def user_count(num1, num2):
    print("Начало count")
    for i in count(num1):
        if i > num2:
            break
        else:
            print(i)


def user_cycl(num1, def_list):
    print("Начало cycle")
    my_count = 1
    for i in cycle(def_list):
        if my_count > num1:
            break
        print(i)
        my_count += 1


start_count = int(argv[1])
finish_count = int(argv[2])
num_cycl = int(argv[3])
months = ['июнь', 'июль', 'август']

user_count(start_count, finish_count)
print(100 * "*")
user_cycl(num_cycl, months)
