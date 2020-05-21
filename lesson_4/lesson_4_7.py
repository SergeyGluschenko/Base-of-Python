def fact(n):
    count = 1
    fact_num = 1
    while count <= n:
        fact_num = fact_num * count
        yield fact_num
        count += 1


n = 8

for el in fact(n):
    print(el)



