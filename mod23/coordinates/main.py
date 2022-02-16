import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)

    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)

    return y / x


file = open('coordinates.txt', 'r')
file_2 = open('result.txt', 'w')
try:

    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            final_list = [str(my_list[0]), str(my_list[1]), str(my_list[2])]
            file_2.write(' '.join(final_list))
            file_2.write('\n')
        except BaseException:
            print("Что-то пошло не так со второй функцией")

except Exception:
    print("Что-то пошло не так с первой функцией")
finally:
    file.close()
    file_2.close()
    print(file.closed)
    print(file_2.closed)