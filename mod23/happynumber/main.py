import random

happy_sum = 0

try:
    with open('numbers.txt', 'w') as numbers_file:
        while happy_sum <= 777:
            happy_sum += int(input('Введите число: '))

            if random.randint(1, 13) == 5:
                raise BaseException('Игра окончена!')
        print('Вы выиграли!')
finally:
    numbers_file.close()
