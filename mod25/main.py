import random

class Inhabitant:

    def __init__(self, name, hub, satiety=50):
        self.name = name
        self.house = hub
        self.satiety = satiety

    def lunch(self):
        if self.house.fridge > 1:
            self.satiety += 1
            self.house.fridge -= 1
            print('{} покушал'.format(self.name))
        else:
            print('Холодильник пуст')

    def job(self):
        self.satiety -= 1
        self.house.safe += 1
        print('{} поработал'.format(self.name))

    def play(self):
        self.satiety -= 1
        print('{} поиграл'.format(self.name))

    def shopping(self):
        if self.house.safe > 0:
            self.house.safe -= 1
            self.house.fridge += 1
            print('{} закупился'.format(self.name))
        else:
            print('Денег в тумбочке нет')

    def is_alive(self):
        if self.satiety >= 0:
            return True
        else:
            return False


class House:

    def __init__(self, refrigerator=50, safe=0):
        self.fridge = refrigerator
        self.safe = safe

    def status(self):
        print('Холодильник: {}, Сейф: {}'.format(self.fridge, self.safe))


class Neiпhborhood:

    def __init__(self, population, location):
        self.number = population
        self.house = location
        self.neighbours = [Inhabitant('', self.house) for _ in range(self.number)]
        for i_neighbour in self.neighbours:
            i_neighbour.name = input('Введите имя соседа: ')

    def is_all_alive(self):
        if not all([i_neighbour.is_alive() for i_neighbour in self.neighbours]):
            print('Все соседи умерли от голода')
            return False
        else:
            return True

    def neighborhood_status(self):
        for i_neighbour in self.neighbours:
            print('{}: Сытость: {},'.format(i_neighbour.name, i_neighbour.satiety))
        print('Бюджет: {}, Запасы провизии: {}'.format(self.house.safe, self.house.fridge))


hut = House()
cohabitation = Neiпhborhood(2, hut)

for i_day in range(1, 366):
    print('\nДень {}'.format(i_day))
    cohabitation.neighborhood_status()
    pause = input('Press any key to continue')
    if cohabitation.is_all_alive():
        for j_neighbour in cohabitation.neighbours:
            odds = random.randint(1, 6)
            print('У {} выпало число: {}'.format(j_neighbour.name, odds))
            if j_neighbour.is_alive():
                if j_neighbour.satiety < 20:
                    j_neighbour.lunch()
                    if j_neighbour.satiety < 0:
                        print('Сосед {} умер от голода на {} день'.format(j_neighbour.name, i_day))
                elif j_neighbour.house.fridge < 10:
                    j_neighbour.shopping()
                elif j_neighbour.house.safe < 50:
                    j_neighbour.job()
                elif odds == 1:
                    j_neighbour.job()
                elif odds == 2:
                    j_neighbour.lunch()
                    if j_neighbour.satiety < 0:
                        print('Сосед {} умер от голода на {} день'.format(j_neighbour.name, i_day))
                else:
                    j_neighbour.play()
    else:
        break

print('Прошёл год эксперимента')
for j_neighbour in cohabitation.neighbours:
    if j_neighbour.is_alive():
        print('Сосед {} выжил'.format(j_neighbour.name))

# зачет!

