import random


class Bodhisattva:

    def __init__(self, name):
        self.name = name
        self.carma = 0

    def __str__(self):
        return '{} имеет {} очков кармы'.format(self.name, self.carma)

    def change_carma(self, points):
        self.carma += points


def one_day(file_name):
    try:
        if random.randint(1, 10) == 1:
            raise BaseException
            if error_type == 1:
                raise KillErrorExeption()

    carma_points = random.randint(1, 7)
    bodhisattva.change_carma(carma_points)

error_type = random.randint(1, 7)
bodhisattva = Bodhisattva('Tom')
day = 0

try:
    with open('carma.log', 'w') as error_file:
        while bodhisattva.carma < 500:
            day += 1
            one_day()

print(f'Набрано {bodhisattva.carma} очков кармы. Поздравляем с просветлением на {day} день!')