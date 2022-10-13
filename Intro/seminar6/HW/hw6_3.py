# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
#
# out
#
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}
#

def CreateDifficultDict(src_ls):
    # создаем пустой словарь
    res_dict = {}
    for nm in src_ls:
        # считываем текущее значение списка элемента словаря,
        # если нет такого ключа в словаре, то создаем пустой список
        if nm[0] in res_dict.keys():
            tmp_ls = res_dict[nm[0]]
        else:
            tmp_ls = []
        # добавляем имя в список и заносим обновленный список обратно в словарь
        tmp_ls.append(nm)
        res_dict[nm[0]] = tmp_ls
    return res_dict


ls = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
my_dict = CreateDifficultDict(ls)
print(my_dict)
