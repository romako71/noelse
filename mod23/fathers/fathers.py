class Parent:

    def __init__(self, parent_name, parent_age, *args):
        self.name = parent_name
        self.age = parent_age
        self.kids = [i_kid for i_kid in args]

    def kidlist(self):
        number = int(input('Сколько детей добавить? '))
        for i_kid in range(number):

            self.kids.append(input)


class Kid:
    conditions = {0: 'Плачет', 1: 'Смеётся'}
    fulness = {0: 'Голодный', 1: 'Сытый'}

    def __init__(self, kid_name, kid_age):
        self.name = kid_name
        self.age = kid_age
        self.condition = 1
        self.satiety = 1
