class Person:

    def __init__(self, name='noname', surname='nosurname', age=None):
        self.__name = name
        self.__surname = surname
        self.set_age(age)

    def __str__(self):
        return 'Имя: {}\t Фамилия: {}\tВозраст: {}'.format(self.__name, self.__surname, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(1, 121):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')

class Employee(Person):

    def __init__(self, name, surname, age, salary=0):
        super.__init__(name, surname, age)
        self.salary = salary

    def salary_calculation(self, wage):
        self.__wage = wage

    def

manny = Person('Федя', 'Стуков', 12)

print(manny)