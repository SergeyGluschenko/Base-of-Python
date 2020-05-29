class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} going')

    def stop(self):
        print(f'{self.name} {self.color} staying')

    def turn(self, direction):
        return direction

    def show_speed(self):
        print(f'Ваша скорость {self.speed}км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed <= 60:
            print(f'Ваша скорость {self.speed}км/ч')
        else:
            print('Вы превыаете скорость - 60 км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed <= 40:
            print(f'Ваша скорость {self.speed}км/ч')
        else:
            print('Вы превыаете скорость - 40 км/ч')


class PoliceCar(Car):

    def is_police_car(self):
        return self.is_police

start_class = Car(11, 'белая', 'копейка', True)
start_class.show_speed()
start_class.go()

town_class = TownCar(44, 'синяя', 'Мазда', True)
town_class.show_speed()
town_class.stop()

police_class = PoliceCar(55, 'синяя', 'Мазда', True)
print(f'Машина полицейская {police_class.is_police}')
print(police_class.turn('left'))

work_car_class = WorkCar(66, 'синяя', 'Мазда', True)
work_car_class.show_speed()
