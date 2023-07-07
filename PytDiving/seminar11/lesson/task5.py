# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длину и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

class Square:
    """Класс Square - описывает прямоугольник. Позвоялет выполнять операции сравнения
    над экземплярами класса Square. """
    def __init__(self, a, b=None):
        self.a = a
        if b:
            self.b = b
        else:
            self.b = a

    def area(self):
        """Площадь прямоугольника"""
        return self.a * self.b

    def perimetr(self):
        """Периметр прямоугольника"""
        return 2 * (self.a + self.b)

    def __str__(self):
        """Печать данных объекта для пользователя - для функций print, str"""
        return f'Данные прямоугольника: Длина={self.a}, ширина={self.b}, ' \
               f'площадь={self.area()}, периметр={self.perimetr()}.'

    def __repr__(self):
        """Печать данных объекта для программиста - в режиме отладки"""
        return f'=Square: {self.a=}, {self.b=}, {self.area()=}, {self.perimetr()=}'

    def __add__(self, other):
        """дандер-метод сложения прямоугольников"""
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Square(new_a, new_b)

    def __sub__(self, other):
        """дандер-метод вычитания прямоугольников"""
        if self.a - other.a < 0 or self.b - other.b < 0:
            raise ValueError
        new_a = self.a - other.a
        new_b = self.b - other.b
        return Square(new_a, new_b)

    def __eq__(self, other):
        """дандер-метод сравнения на равенство прямоугольников"""
        return self.area() == other.area()

    def __ne__(self, other):
        """дандер-метод сравнения на неравенство прямоугольников"""
        return self.area() != other.area()

    def __gt__(self, other):    # больше
        """дандер-метод сравнения - "больше" прямоугольников"""
        return self.area() > other.area()

    def __ge__(self, other):    # больше или равно
        """дандер-метод сравнения - "больше или равно" прямоугольников"""
        return self.area() >= other.area()

    def __lt__(self, other):    # меньше
        """дандер-метод сравнения - "меньше" прямоугольников"""
        return self.area() < other.area()

    def __le__(self, other):    # меньше или равно
        """дандер-метод сравнения - "меньше или равно" прямоугольников"""
        return self.area() <= other.area()


sq1 = Square(10, 6)
sq2 = Square(2, 1)

sq3 = sq1 + sq2
sq4 = sq1 - sq2

print(f'{sq1.a=}, {sq1.b=}, {sq1.area()=}, {sq1.perimetr()=}')
print(f'{sq1.a=}, {sq1.b=}, {sq1.area()=}, {sq1.perimetr()=}')

print(repr(sq3))    #вызов метода __repr__()
print(sq4)  #будет автоматически __str__() вызван

# __repr__() надо явно вызывать: print(repr(x))  - вот так.
# Если __str__() не определен, то автоматически __repr__() вызывается.

print(sq3.perimetr())
print(sq4.perimetr())

print(sq1 > sq2)
print(sq1 < sq2)
print(sq1 == sq2)
print(sq1 != sq2)
print(sq1 >= sq2)
print(sq1 <= sq2)