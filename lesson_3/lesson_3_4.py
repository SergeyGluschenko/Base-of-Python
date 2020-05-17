def my_func(x, y):
    print(x ** abs(y))


my_func(2, -6)


def my_func2(x, y):
    def_result = 1  # на случай, если степень будет равна ноль
    count = 1
    while count <= abs(y):
        def_result *= x
        count += 1
    print(def_result)


my_func2(2, -6)
