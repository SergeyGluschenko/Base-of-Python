def my_func(def_num1, def_num2, def_num3):
    list_def = [def_num1, def_num2, def_num3]
    list_def.remove(min(list_def))
    print(sum(list_def))


my_func(7, 4, 125)


def my_func2(a, b, c):
    if a < b:
        if a < c:
            print(b + c)
        else:
            print(a + b)
    else:
        if b < c:
            print(a + c)
        else:
            print(a + b)


my_func2(7, 4, 125)