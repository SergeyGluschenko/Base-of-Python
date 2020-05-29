class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        res = 0
        for key, val in self._income.items():
            res += val
        return res

list_1 = {'wage': 10, 'bonus': 20}


b = Position('Ваня', 'Глу', 'Президент', list_1)
print(f'Полное имя человека {b.get_full_name()}')
print(f'Доход с учетом премии {b.get_total_income()}')



