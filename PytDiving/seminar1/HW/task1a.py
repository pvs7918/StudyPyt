# 1.
# a. Написать программу, которая будет выводить в консоль ёлочку заданной высоты

h = int(input('Введите высоту ёлочки: '))

for i in range(h):
    num_stars = i * 2 + 1  # количество звезд в текущей строке
    print(' ' * (h - i - 1), '*' * (num_stars))
