import math

class Auto:

    """Направление движения задаётся вводом курсового угла, выраженного в градусах."""

    def __init__(self, x_position=0, y_position=0, direction=0):
        self.x_pos = x_position
        self.y_pos = y_position
        self.direction = direction * math.pi / 180

    def __str__(self):
        course = round(self.direction * 180 / math.pi)
        return 'Автомобиль находится в точке: {}, {} (км). Движется в напаравлении: {} градусов.\n'.format(self.x_pos, self.y_pos, course)

    def move(self, mileage):
        self.x_pos += round(mileage * math.sin(self.direction), 2)
        self.y_pos += round(mileage * math.cos(self.direction), 2)

        return  self.x_pos, self.y_pos

    def turn(self, change_direction_angle):
        self.direction += change_direction_angle * math.pi / 180


class Bus(Auto):

    __capacity = 60
    __fare = 0.37

    def __init__(self, x_position=0, y_position=0, direction=0, passengers=0, cash=0):
        super().__init__(x_position, y_position, direction)
        self.__passengers = passengers
        self.__cash = cash
        print('\nАвтобус начинает движение из точки: {}, {} (км) в напаравлении: {} градусов'.format(self.x_pos, self.y_pos, self.direction))

    def __str__(self):
        course = round(self.direction * 180 / math.pi)
        return '\nАвтобус:\n\tнаходится в точке: {}, {}\n\tДвижется в напаравлении: {}\n\tВезёт {} пассажиров.' \
               '\n\tВ кассе {} денег'.format(self.x_pos, self.y_pos, course, self.__passengers, self.__cash)

    def boarding(self, passengers):
        if passengers >= 0:
            if passengers + self.__passengers <= self.__capacity:
                print(f'\nПосадка в автобус: {passengers} пассажиров.')
                self.__passengers += passengers
            else:
                passengers_boarded = self.__capacity - self.__passengers
                passengers_left = passengers - passengers_boarded
                self.__passengers = self.__capacity
                print(f'\nАвтобус полный.\n\tУдалось посадить только {passengers_boarded} пассажиров. Все 60 мест заняты'
                      f'\n\t{passengers_left} пассажиров остались на остановке.')
        else:
            print('Ошибка. Количество пассажиров не может быть отрицательной величиной.')

    def unload(self, passengers):
        if passengers < 0:
            print('\nОшибка. Количество пассажиров не может быть отрицательной величиной')
        elif passengers > self.__passengers:
            print(f'\nВ автобусе всего {self.__passengers} пассажиров. Все высажены. Автобус пуст')
            self.__passengers = 0
        else:
            self.__passengers -= passengers
            print(f'\nВысадка из автобуса: {passengers} пассажиров.')

    def move(self, mileage):
        self.x_pos += round(mileage * math.sin(self.direction), 2)
        self.y_pos += round(mileage * math.cos(self.direction), 2)
        self.__cash += self.__passengers * mileage * self.__fare




auto1 = Auto()
bus1 = Bus()

bus1.boarding(25)
bus1.turn(60)
bus1.move(2)
print(bus1)

bus1.boarding(36)
bus1.turn(60)
bus1.move(2)
print(bus1)

bus1.unload(47)
bus1.turn(120)
bus1.move(2)
print(bus1)

bus1.unload(38)
bus1.turn(60)
bus1.move(2)

print(bus1)


