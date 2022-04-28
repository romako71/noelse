class Parent:

    def __init__(self, parent_name, parent_age):
        self.name = parent_name
        self.age = parent_age
        self.kids = []

    def new_kids(self):
        number = int(input('Сколько детей добавить? '))
        for _ in range(number):
            new_kid_name = input('Введиет имя ребёнка: ')
            new_kid_age = input('Введите возраст ребёнка: ')
            if (self.age - new_kid_age) < 16:
                print('Разница в возрасте выглядит неприемлемо неправдоподобной. В добавлении этого ребёнка отказано')
            else:
                new_kid = Kid(new_kid_name, new_kid_age)
                self.kids.append(new_kid)


class Kid:
    conditions = {0: 'Плачет', 1: 'Смеётся'}
    fulness = {0: 'Голодный', 1: 'Сытый'}

    def __init__(self, kid_name, kid_age):
        self.name = kid_name
        self.age = kid_age
        self.condition = 1
        self.satiety = 1
