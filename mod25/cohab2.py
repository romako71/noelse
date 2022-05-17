import random


class House:

    def __init__(self):
        self.__residents = []
        self.safe = 100
        self.fridge = 50
        self.cat_food = 30
        self.dirt = 0

    def __str__(self):
        print('Живут:', end=' ')
        for i_resident in self.__residents:
            print('{}({})\t'.format(i_resident.name, i_resident.role), end='')
        return ''

    def add_resident(self, creation):
        if isinstance(creation, (Husband, Wife, Kinder)):
            self.__residents.append(creation)


class Human:

    def __init__(self, name='noname', satiety=30, happyness=100):
        self.name = name
        self.satiety = satiety
        self.happyness = happyness
        self.hub = None

    def __str__(self):
        return self.name

    def lunch(self, ratio, fridge):
        if fridge > ratio:
            self.satiety += ratio
            fridge -= ratio
        else:
            self.satiety += fridge
            fridge = 0
        print('{} съел {} еды. Сытость {}'.format(self.name, ratio, self.satiety))

        return fridge

    def petting(self):
        self.happyness += 5
        self.satiety -= 10


class Husband(Human):
    role = 'муж'

    def __init__(self, name='noname', satiety=30, happyness=100):
        super().__init__(name, satiety, happyness)
        self.income = 0

    def __str__(self):
        return self.name

    def play(self):
        self.satiety -= 10
        self.happyness += 20
        print('{} поиграл'.format(self.name))

    def work(self, safe):
        safe += 150
        self.satiety -= 10
        return safe


class Wife(Human):
    role = 'жена'

    def __init__(self, name='noname', satiety=30, happyness=100):
        super().__init__(name, satiety, happyness)
        self.__fur_coats = 0

    def buy_food(self, storage, safe):
        self.satiety -= 10
        if safe > 100:
            stock_growth = 100
            storage += 100
            safe -= 100
        else:
            stock_growth = safe
            storage += safe
            safe = 0
        print('Добавлено {} еды. В тумбочке {} денег'.format(stock_growth, safe))

    def buy_fur_coat(self, safe):
        if safe >= 350:
            safe -= 350
            self.__fur_coats += 1
        return safe

class Kinder(Human):

    role = 'ребёнок'

    def go_to_school(self):
        self.satiety -= 10
        self.happyness -=10

class Cat:






home = House()
wif = Wife('Io')
hus = Husband('Bob')
kind = Kinder('Zu')


home.add_resident(hus)
home.add_resident(wif)
home.add_resident(kind)
print(home)

# def work(self):
#     safe += 150
#     print('В тумбочке +150 денег')
#
# class Wife:
#
#     def shopping(self):
#         if self.house.safe > 0:
#             self.house.safe -= 1
#             self.house.fridge += 1
#             print(' закупился'.format(self.name))
#         else:
#             print('Денег в тумбочке нет')
#
#     def is_alive(self):
#         if self.satiety >= 0:
#             return True
#         else:
#             return False
#
#
# class House:
#
#     def __init__(self, refrigerator=50, safe=0):
#         self.fridge = refrigerator
#         self.safe = safe
#
#     def status(self):
#         print('Холодильник: {}, Сейф: {}'.format(self.fridge, self.safe))
#
#
# class Neiпhborhood:
#
#     def __init__(self, population, location):
#         self.number = population
#         self.house = location
#         self.neighbours = [Inhabitant('', self.house) for _ in range(self.number)]
#         for i_neighbour in self.neighbours:
#             i_neighbour.name = input('Введите имя соседа: ')
#
#     def is_all_alive(self):
#         if not all([i_neighbour.is_alive() for i_neighbour in self.neighbours]):
#             print('Все соседи умерли от голода')
#             return False
#         else:
#             return True
#
#     def neighborhood_status(self):
#         for i_neighbour in self.neighbours:
#             print('{}: Сытость: {},'.format(i_neighbour.name, i_neighbour.satiety))
#         print('Бюджет: {}, Запасы провизии: {}'.format(self.house.safe, self.house.fridge))