# Создайте класс Сотрудник.

# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

import random
from task3 import Person


class Stuff(Person):
    def __init__(self, *args, **kwargs):
        self.id = random.randint(100000, 999999)
        super().__init__(*args, **kwargs)

    @property               # это делает из метода атрибут
    def access_lvl(self):
        str_id = str(self.id)
        list_id_numbers = sum(list(map(int, str_id)))
        return list_id_numbers % 7

s1 = Stuff('Илья', 'Петрович', 'Иванов', 12345, 32)
print(f'{s1.id = }, {s1.access_lvl = }')