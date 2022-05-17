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