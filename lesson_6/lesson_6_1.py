import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color
        self.running()

    def running(self):
        while True:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(13)



color = ['красный', 'желтый', 'зеленый']
a = TrafficLight(color)


