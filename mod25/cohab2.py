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
        print('{} обедает. Сытость {}. Остаток в холодильнике: {}'.format(self.name, self.satiety, fridge))
        return fridge

    def petting(self):
        self.happyness += 5
        self.satiety -= 10
        print('{} погладил кота'.format(self.name))

    def is_alive(self):
        if (self.satiety >= 0) and (self.happyness >= 10):
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
        print('{} поиграл'.format(self.name))

    def work(self, safe):
        safe += 150
        final_statistics[0] += 150
        self.satiety -= 10
        print('{} поработал'.format(self.name))
        return safe

    def day_in_the_life(self, cash, storage):
        if self.satiety < 15:
            storage = self.lunch(storage)
        elif cash < 80:
            cash = self.work(cash)
        else:
            choice = random.randint(1, 3)
            if choice == 1:
                self.play()
            elif choice == 2:
                cash = self.work(cash)
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
            final_statistics[1] += 60
            storage += 60
            safe -= 60
        else:
            final_statistics[1] += safe
            storage += safe
            safe = 0
        print('{} сходила в магазин. В холодильнике {} еды. В тумбочке {} денег'.format(self.name, storage, safe))
        return storage, safe

    def buy_fur_coat(self, safe):
        if safe >= 350:
            safe -= 350
            self.__fur_coats += 1
            self.happyness += 60
            final_statistics[2] += 1
            print('Шуб в шубохранилище: {}'.format(self.__fur_coats))
        else:
            print('Денег на шубу пока не хватает')
        return safe

    def cleaning(self, dirt):
        if dirt > 100:
            dirt -= 100
        else:
            dirt = 0
        print('{} убиралась. Грязи в доме осталось: {}'.format(self.name, dirt))
        return dirt

    def day_in_the_life(self, storage, cat_storage, cash, mud):
        if self.satiety < 20:
            storage = self.lunch(storage)
        elif (storage < 40) and (cash > 0):
            storage, cash = self.buy_food(storage, cash)
        elif (cat_storage <= 10) and (cash > 0):
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
        if self.satiety < 20:
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

    def is_alive(self):
        if self.satiety >= 0:
            return True
        else:
            return False

    def day_in_the_life(self, storage, mud):
        if self.satiety <= 30:
            if storage >= 10:
                self.satiety += 20
                storage -= 10
            else:
                self.satiety += 2 * storage
                storage = 0
            print('Кот {} кормился. Кошачьей еды осталось: {}'.format(self.name, storage))
        else:
            choice = random.randint(1, 2)
            if choice == 1:
                self.satiety -= 10
                print('Кот {} спал'.format(self.name))
            else:
                mud = self.spoil_walls(mud)
                print('Кот {} драл обои. Грязи в доме: {}'.format(self.name, mud))
        return storage, mud

def day_in_the_life(hub):
    if hub.dirt > 90:
        for i_subject in hub.residents:
            if not isinstance(i_subject, Cat):
                i_subject.happyness -= 10
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
            hub.cat_food, hub.dirt = j_subject.day_in_the_life(hub.cat_food, hub.dirt)


final_statistics = [0] * 3
home = House()
wif2 = Wife('Lu')
hus2 = Husband('Bob')
kin1 = Kinder('Jimmy')
cat1 = Cat('Tom')
cat2 = Cat('Leopold')
cat3 = Cat('Basilio')
home.add_resident(hus2)
home.add_resident(wif2)
home.add_resident(kin1)
home.add_resident(cat1)
home.add_resident(cat2)
home.add_resident(cat3)


i_day = 0
all_are_alive = True
while i_day < 365:
    print()
    home.dirt += 5
    i_day += 1
    print('День {}'.format(i_day))
    home.status()
    print()
    if not home.is_all_alive():
        all_are_alive = False
        break
    else:
        day_in_the_life(home)

print()
if all_are_alive:
    final_statistics[0] += 50
    final_statistics[1] = final_statistics[1] + 80 - home.fridge - home.cat_food
    print('Прошёл год.\n\tДенег заработано: {}\n\tЕды съедено: {}\n\tШуб куплено: {}'.format(
        final_statistics[0], final_statistics[1], final_statistics[2]
    ))
