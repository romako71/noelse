import math

class Circle:

    def __init__(self, crd_X=0, crd_Y=0, rds=1):
        self.X = crd_X
        self.Y = crd_Y
        self.radius = rds

    def circle_square(self):
        sqr = math.pi * self.radius ** 2
        return sqr

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def magnify(self, radius_rate):
        new_rds = self.radius * radius_rate
        new_circle = Circle(self.X, self.Y, new_rds)
        return new_circle

    def crossing(self, circle1):
        if ((circle1.X - self.X) ** 2 + (circle1.Y - self.Y) ** 2) <= (circle1.radius + self.radius) ** 2:
            print('Круги пересекаются')
        else:
            print('Круги не пересекаются')

    def print_circle(self):
        print('\nКоордината X: {},\nКоордината Y: {}\nРадиус: {}'.format(self.X, self.Y, self.radius))

ring1 = Circle(1, 1, 3)
ring2 = Circle(1, 0, 2)
ring3 = ring1.magnify(3)
print('Площадь первого круга: {}\nПериметр первой окружности: {}\n'.format(ring1.circle_square(), ring1.perimeter()))
ring3.print_circle()
ring1.crossing(ring2)

