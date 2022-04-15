class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def harvesting(self):
        if self.state == 3:
           self.state = 0
        self.print_state()

    def grow(self):
        if self.state < 3:
           self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))

class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

class Gardener:

    def __init__(self, gardener_name, sample_garden):
        self.name = gardener_name
        self.garden = sample_garden

    def garden_care(self):
        print('Грядка обрабатывается садовником {}.'.format(
            self.name
        ))
        for i_potato in self.garden():
            i_potato.grow()

    def garden_harvesting(self):
        for i_potato in self.garden.potatoes:
            i_potato.harvesting()
        print('Урожай собран. Ждите нового урожая')




my_garden = PotatoGarden(5)
my_gardener = Gardener('Семён Семёныч', my_garden)
my_garden.are_all_ripe()
while True:
    if my_garden.are_all_ripe():
        my_gardener.garden_harvesting()
    else:
        my_gardener.garden_care()
    if input('Введите 1, если хотите продолжить ждать урожай.\n'
             'Введите любой другой символ, если сезон закончен') != '1':
        break
