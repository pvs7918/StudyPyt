# 📌 Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.

def get_number():
    while True:
        try:
            num = input('Enter an integer or float: ')
            if '.' in num:
                return float(num)
            return int(num)
        except ValueError as e:
            print('You introduced not number')

get_number()