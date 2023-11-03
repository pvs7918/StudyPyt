# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.

def get_val_in_dict(dict_work: dict, key, default_value):
    try:
        return dict_work[key]
    except Exception:
        return default_value


dic = {1: 2, 2: 4, 3: 'dfgdgfa'}
print(get_val_in_dict(dic, 'erwer', 0))
print(get_val_in_dict(dic, 1, 0))
