class Auto:

    def __init__(self, x_position, y_position, direction):
        self.__x_pos = x_position
        self.__y_pos = y_position
        self.__direction = direction

    def __str__(self):
        return 'Автомобиль находится в точке: {}, {}. Движется в напаравлении: {}'.format(self.__x_pos, self.__y_pos, self.__direction)

    def move(self):
        pass

    def turn(self):
        pass


class Bus(Auto):

    def __init__(self, x, y, direct, passengers, cash=0):
        super().__init__(x, y, direct)
        self.__passengers = passengers
        self.__cash = cash

    def __str__(self):
        return 'Автобус:\n\tнаходится в точке: {}, {}\n\tДвижется в напаравлении: {}\n\tВезёт {} пассажиров' \
               '\n\tВ кассе {} денег'.format(self.__x_pos, self.__y_pos, self.__direction, self.__passengers, self.__cash)



auto1 = Auto(0, 0, 0)
bus1 = Bus(0, 0, 0, 0)

print(auto1)
print(bus1)
#

