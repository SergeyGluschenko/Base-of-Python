class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки Pen')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки Pencil')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки Handle')


start_class = Stationery('Нечто')
start_class.draw()

pen_class = Pen('Pen')
pen_class.draw()

pencil_class = Pencil('pencil')
pencil_class.draw()

handle_class = Handle('Handle')
handle_class.draw()