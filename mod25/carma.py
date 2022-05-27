import random

class Bodhisattva:

    def __init__(self, name):
        self.__name = name
        self.__carma = 0

    def __str__(self):
        return '{} имеет {} очков кармы'.format(self.__name, self.__carma)

    def change_carma(self, points):
        self.__carma += points

    def get_carma(self):
        return self.__carma


def one_day(file_name, next_day):
    try:
        if random.randint(1, 10) == 1:
            raise Exception
        return random.randint(1, 7)
    except:
        fate = random.randint(1, 5)
        # TODO тут надо не просто сообщение, а raise-ить ошибки, ошибки надо создать свои, как это сделано тут https://github.com/tortoise/tortoise-orm/blob/develop/tortoise/exceptions.py
        if fate == 1:
            message = 'KillError'
        elif fate == 2:
            message = 'DrunkError'
        elif fate == 3:
            message = 'CarCrashError'
        elif fate == 4:
            message = 'GluttonyError'
        elif fate == 5:
            message = 'DepressionError'
        else:
            message = 'GlobalKarmaError'
        file_name.write('День {}: {}\n'.format(next_day, message))
        return 0


error_type = random.randint(1, 7)
bodhisattva = Bodhisattva('Tom')
trial_day = 0

with open('carma.log', 'w', encoding='utf-8') as error_file:
    while bodhisattva.get_carma() < 500:
        trial_day += 1
        plus_carma = one_day(error_file, trial_day)
        bodhisattva.change_carma(plus_carma)

print(f'Набрано {bodhisattva.get_carma()} очков кармы. Поздравляем с просветлением на {trial_day} день!')
