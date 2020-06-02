from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param, count):
        self._param = param
        self.count = count
        self._material = []

    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):

    @property
    def material(self):
        coat_mat = (self._param / 6.5 + 0.5) * self.count
        return round(coat_mat, 2)


class Suit(Clothes):

    @property
    def material(self):
        suit_mat = (2 * self._param + 0.5) * self.count
        return round(suit_mat, 2)


coat_class = Coat(2, 4)
print(f'На пальто пошло {coat_class.material} едениц материала')

suit_class = Suit(2, 4)
print(f'На пальто пошло {suit_class.material} едениц материала')

print(f'Всего материала на производство - {coat_class.material + suit_class.material}')