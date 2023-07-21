# 2.	Создайте класс студента.
# 3.	Используя дескрипторы проверяйте ФИО на первую заглавную букву
# и наличие только букв.
# 4.	Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# 5.	Для каждого предмета можно хранить оценки (от 2 до 5)
# и результаты тестов (от 0 до 100).
# 6.	Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.
import random


class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше '
                             f'или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть '
                             f'меньше {self.max_value}')


# class Text:
#     def __init__(self, param =''):
#         self.param = param
#
#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name
#
#     def __set__(self, instance, value):
#         if self.param(value):
#             setattr(instance, self.param_name, value)
#         else:
#             raise ValueError(f'Значение "{value}" не отвечает требованиям {self.param_name}')
#
#         if value.istitle() != True:
#             raise TypeError(f'Значение "{value}" начинается не с заглавной буквы.')
#         elif value.isalpha() != True:
#             raise TypeError(f'Значение "{value}" должно содержать только буквы.')
#         else:
#             self.param_name = value

class Student:
    marks: dict = {int: (Range(2, 5), str)}
    fullname: str  # с помощью класса определяем дескриптор с допустимыми значениями для атрибута - значинается с заглавной буквы
    test_marks_dict = {
        1: (5, 'math')}
    # словарь средних баллов по тестам для каждого предмета
    _test_avg_marks_dict: dict = {str: Range(2, 5)}
    # средний бал по оценкам всех предметов вместе взятых
    _common_avg_mark: float

    def __init__(self, fullname: str, marks: dict):
        # ФИО студента
        self.fullname = fullname
        # словарь отметок студента по тестам
        self.marks = marks

    def __str__(self):
        res_text = f'Student: {self.fullname}\nотметки: {self.marks}\n{self.avg}'
        return res_text

    @property
    def avg(self):
        self._test_avg_marks_dict = {}
        # метод считает средний балл по каждому предмету и общий балл по всем предметам
        summ = 0
        cnt = 0
        for cur_mark in self.marks.values():
            summ += cur_mark[0]
            cnt += 1
            #средние баллы по предметам хранятся в виде сумма балов по предмету и количества отметок
            avg_mark, avg_cnt = self._test_avg_marks_dict.get(cur_mark[1], (0, 0))
            self._test_avg_marks_dict[cur_mark[1]] = (avg_mark + cur_mark[0], avg_cnt + 1)

        res_text = f'Сумма отметок: {summ}, количество: {cnt}.\nСредние баллы по предметам:\n'

        for key, val in self._test_avg_marks_dict.items():
            res_text += f'предмет: {key} - средний балл: {val[0]/val[1]:.1f}\n'
        res_text += f'Общий средний балл: {summ / cnt:.1f}\n'
        return res_text


if __name__ == "__main__":
    # общий список школьных предметов
    subjects = {'Математика': 'mat', 'Русский язык': 'rus', 'Литература': 'lit', 'История': 'his',
                'Английский язык': 'eng', 'Физика': 'fiz', 'Химия': 'che'}

    # список имен студентов
    student_names = ["Иванов Иван", "Сидоров Петр", "Петрова Мария"]

    subjects_eng_name_list = list(subjects.values())
    # формируем stud_list список объектов класса Student, отметки по тестам заполняем слуайным образом
    stud_list = []
    for name in student_names:
        # формируем словарь отметок студента через random
        marks = {}
        for i in range(1, random.randint(6, 11)):  # создаем 3-5 отметки по тестам
            marks[i] = (random.randint(2, 5), random.choice(subjects_eng_name_list))
        stud_list.append(Student(name, marks))
        # выводим данные текущего студента. Общие отметки выводятся через свойство avg в методе __str__
        print(stud_list[-1])
