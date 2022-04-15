class Property():

    def __init__(self, worth):
        self.set_worth(worth)

    def __str__(self):
        return f'Стоимость актива составляет {self.__worth} рублей'

    def set_worth(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth


    def tax_rate(self):
        tax = self.__worth/400
        return f'Базовый налог составляет {tax} рублей'

class Apartment(Property):

    def __str__(self):
        return f'Стоимость квартиры составляет {self.get_worth()}'

    def tax_rate(self):
        tax = self.get_worth() / 1000
        return f'Налог на квартиру составляет {tax} рублей'

class Car(Property):

    def __str__(self):
        return f'Стоимость машины составляет {self.get_worth()}'

    def tax_rate(self):
        tax = self.get_worth() / 200
        return f'Налог на машину составляет {tax} рублей'

class CountryHouse(Property):

    def __str__(self):
        return f'Стоимость дачи составляет {self.get_worth()}'

    def tax_rate(self):
        tax = self.get_worth() / 500
        return f'Налог на дачу составляет {tax} рублей'

property = Property(5000)
print(property)
print(property.tax_rate())

apartment = Apartment(1000000)
print(apartment)
print(apartment.tax_rate())

car = Car(500000)
print(car)
print(car.tax_rate())

country_house = CountryHouse(200000)
print(country_house)
print(country_house.tax_rate())