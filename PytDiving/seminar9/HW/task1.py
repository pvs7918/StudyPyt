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


def read_csv_and_decide_equations():
    with open('task1.csv', 'r', newline='', encoding='utf-8') as f1:
        csv_file = csv.reader(f1, delimiter=",")
        res_dict = {}
        for row in csv_file:
            a, b, c = row.split()
            res_dict[a, b, c] = solving_quad_equation(a, b, c)
    return res_dict


def save_to_json(res_dict):
    with open('task1.json', 'w', encoding='utf-8') as f1:
        json.dump(res_dict, f1, ensure_ascii=False, indent=4)

