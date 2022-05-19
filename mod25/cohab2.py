import random

class House:

    def __init__(self, address='без адреса'):
        self.address = address
        self.residents = []
        self.safe = 100
        self.fridge = 50
        self.cat_food = 30
        self.dirt = 0

    def __str__(self):
        print('В доме {} живут:'.format(self.address), end=' ')
        for i_resident in self.residents:
            print('{}({})\t'.format(i_resident.name, i_resident.role), end='')
        print()
        return ''

    def add_resident(self, creation):
        if isinstance(creation, (Husband, Wife, Kinder, Cat)):
            self.residents.append(creation)

    def is_all_alive(self):
        if not all([i_cohabitator.is_alive() for i_cohabitator in self.residents]):
            print('Эксперимент не удался. Кто-то умер от голода')
            return False
        else:
            return True

    def status(self):
        print('В доме {} живут: '.format(self.address))
        for i_cohabitator in self.residents:
            if isinstance(i_cohabitator, Cat):
                print('\t{} {}\tсытость: {}'.format(i_cohabitator.role, i_cohabitator.name, i_cohabitator.satiety))
            else:
                print('\t{} {}\tсытость: {}\tсчастье: {}'.format(i_cohabitator.role, i_cohabitator.name, i_cohabitator.satiety, i_cohabitator.happyness))
        print('\tВ холодильнике еды: {}\tКошачьей еды: {}\t Денег в тумбочке: {}\tГрязи: {}'.format(
            self.fridge, self.cat_food, self.safe, self.dirt
        ))

class Human:

    def __init__(self, name='noname', hub=None):
        self.house = hub
        self.name = name
        self.satiety = 30
        self.happyness = 100

    def __str__(self):
        return '{}:\t сытость {},\t счастья {}'.format(self.name, self.satiety, self.happyness)

    def lunch(self, fridge):
        if fridge > 30:
            self.satiety += 30
            fridge -= 30
        else:
            self.satiety += fridge
            fridge = 0
        print('{} пообедал. Сытость {}. Остаток в холодильнике: {}\n'.format(self.name, self.satiety, fridge))
        return fridge

    def petting(self):
        self.happyness += 5
        self.satiety -= 10
        print('{} погладил кота\n'.format(self.name))

    def is_alive(self):
        if self.satiety >= 0:
            return True
        else:
            return False

class Husband(Human):
    role = 'муж'

    def __init__(self, name='noname', hub=None):
        super().__init__(name)
        self.income = 0

    def play(self):
        self.satiety -= 10
        self.happyness += 20
        print('{} поиграл\n'.format(self.name))

    def work(self, safe):
        safe += 150
        self.satiety -= 10
        return safe

    def day_in_the_life(self, cash, storage):
        if self.satiety < 15:
            storage = self.lunch(storage)
        elif cash < 80:
            cash = self.work(cash)
        else:
            choice = random.randint(1, 2)
            if choice == 1:
                self.play()
            else:
                self.petting()
        return cash, storage

class Wife(Human):
    role = 'жена'

    def __init__(self, name='noname'):
        super().__init__(name)
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
        print('{} сходила в магазин. В холодильнике {} еды. В тумбочке {} денег'.format(self.name, storage, safe))
        return storage, safe

    def buy_fur_coat(self, safe):
        if safe >= 350:
            safe -= 350
            self.__fur_coats += 1
            print('Шуб в шубохранилище: {}'.format(self.__fur_coats))
        else:
            print('Денег на шубу пока не хватает')
        return safe

    def cleaning(self, dirt):
        if dirt > 100:
            dirt -= 100
        else:
            dirt = 0
        print('Грязи в доме осталось: {}'.format(dirt))
        return dirt

    def day_in_the_life(self, storage, cat_storage, cash, mud):
        if self.satiety < 25:
            storage = self.lunch(storage)
        elif (storage < 100) and (cash > 0):
            storage, cash = self.buy_food(storage, cash)
        elif (cat_storage <= 15) and (cash > 0):
            cat_storage, cash = self.buy_food(cat_storage, cash)
        elif mud >= 60:
            mud = self.cleaning(mud)
        elif cash >= 350:
            cash = self.buy_fur_coat(cash)
        else:
            self.petting()
        return storage, cat_storage, cash, mud

class Kinder(Human):

    role = 'ребёнок'

    def day_in_the_life(self, storage):
        if self.satiety < 25:
            storage = self.lunch(storage)
        else:
            self.petting()
        return storage

class Cat:

    role = 'кот'

    def __init__(self, name='unnamed cat'):
        self.name = name
        self.satiety = 30

    def __str__(self):
        return 'Кот {}:\t сытость {}'.format(self.name, self.satiety)

    def feed(self, cat_storage):
        if cat_storage > 10:
            cat_storage -= 10
            self.satiety += 20
        else:
            self.satiety += cat_storage * 2
            cat_storage = 0
        print('{} поел. Сытость {}. Остаток кошачьей еды: {}'.format(self.name, self.satiety, cat_storage))
        return cat_storage

    def spoil_walls(self, dirt):
        self.satiety -= 10
        dirt += 5
        return dirt

    def sleep(self):
        self.satiety -= 10

    def is_alive(self):
        if self.satiety >= 0:
            return True
        else:
            return False

def day_in_the_life(hub):
    for j_subject in hub.residents:
        if isinstance(j_subject, Husband):
            hub.safe, hub.fridge = j_subject.day_in_the_life(hub.safe, hub.fridge)
        elif isinstance(j_subject, Wife):
            hub.fridge, hub.cat_food, hub.safe, hub.dirt = j_subject.day_in_the_life(
                hub.fridge, hub.cat_food, hub.safe, hub.dirt
            )
        elif isinstance(j_subject, Kinder):
            hub.fridge = j_subject.day_in_the_life(hub.fridge)
        else:
            pass



home = House()
wif2 = Wife('Lu')
hus2 = Husband('Bob')
kin1 = Kinder('Jimmy')
cat1 = Cat('Tom')
home.add_resident(hus2)
home.add_resident(wif2)
home.add_resident(kin1)
home.add_resident(cat1)


i_day = 0
while i_day < 5:
    i_day += 1
    print('День {}'.format(i_day))
    home.status()
    print()
    if not home.is_all_alive():
        all_are_alive = False
        break
    else:
        day_in_the_life(home)




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

#
#     def neighborhood_status(self):
#         for i_neighbour in self.neighbours:
#             print('{}: Сытость: {},'.format(i_neighbour.name, i_neighbour.satiety))
#         print('Бюджет: {}, Запасы провизии: {}'.format(self.house.safe, self.house.fridge))