class Road:
    def __init__(self, width, length, height_cover):
        self._lenght = length
        self._width = width
        self._height_cover = height_cover
        ''' решил добвить высоту height_cover, т.к. иp условия не ясно, 
        где программа должна брать это не константное значене'''

    def get_weight_road(self):
        res = self._width * self._lenght * self._height_cover * 25 / 1000
        return res


my_road = Road(20, 5000, 5)
print(f'Вес дороги будет {my_road.get_weight_road()} тонн')
