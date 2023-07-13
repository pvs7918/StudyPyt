# Напишите следующие функции:
# ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения
#  с каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы функции
#  в json файл.
from random import randint
from typing import Callable
import csv
import json




@solving
def solving_quad_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b
    else:
        return None


def gen_csv(cnt: int, n_min, n_max):
    with open('task1.csv', 'w', newline='', encoding='utf-8') as f1:
        csv_write = csv.DictWriter(f1,
                                   fieldnames=["a", "b", "c"],
                                   dialect='excel',
                                   quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        for i in range(cnt):
            a = randint(n_min, n_max + 1)
            b = randint(n_min, n_max + 1)
            c = randint(n_min, n_max + 1)
            csv_write.writerow([a, b, c])





def save_to_json(res_dict):
    def read_csv_and_decide_equations():
        with open('task1.csv', 'r', newline='', encoding='utf-8') as f1:
            csv_file = csv.reader(f1, delimiter=",")
            res_dict = {}
            for row in csv_file:
                a, b, c = row.split()
                res_dict[a, b, c] = solving_quad_equation(a, b, c)
        return res_dict
    return read_csv_and_decide_equations

    with open('task1.json', 'w', encoding='utf-8') as f1:
        json.dump(res_dict, f1, ensure_ascii=False, indent=4)





# def outer() -> Callable:
#     num_range = int(input('Input number 1 -- 100: '))
#     attempts = int(input('Input number of attempts (1 -- 10): '))
#     num_sc = randint(1, num_range)
#
#     def inner() -> None:
#         nonlocal num_range, attempts
#         while attempts:
#             print(f'left {attempts} attempts.', end=' ')
#             attempts -= 1
#             num = int(input('Input a number: '))
#             if num == num_sc:
#                 print(f'Number found: {num}')
#                 break
#             else:
#                 advice = ['lesser', 'greater']
#                 print(f'Your number is {advice[num > num_sc]} then right')
#         else:
#             print(f'You loose. Right number is {num_sc}')
#
#     return inner


def main():
    # game = outer()
    # game()

    solving_quad_equation(4, 5, 2)


if __name__ == '__main__':
    main()
