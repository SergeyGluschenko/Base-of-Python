class Matrix:
    def __init__(self, list):
        self.list = list
        print(self.list)

    def __str__(self):
        c = ''
        for i in self.list:
            w = ''
            for b in i:
                w += (str(b) + '\t')
            c += (w + '\n')
        return c

    def __add__(self, other):
        for i in range(len(self.list)):
            list_j = ''
            for j in range(len(self.list[i])):
                temp = self.list[i][j] + other[i][j]
                list_j += str(temp) + '\t'
            print(list_j)


mat = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat, end='')
print(100 * '*')
new_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

mat + new_list


