# ✔Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def my_fibo(numbers_limit):
    numbers_count = 1
    f = 0 #первое число из текущей пары
    yield numbers_count, f

    s = 1 #второе число из текущей пары
    numbers_count += 1
    yield numbers_count, s

    while numbers_count < numbers_limit:
        sum = f + s #следущее число, равна сумме предыдущих чисел Фибоначчи
        f = s
        s = sum
        numbers_count += 1
        yield numbers_count, sum


for i in my_fibo(20): #вывести первые 20 чисел Фибоначчи
    print(*i)   #распаковывай кортеж перед печатью (порядковый номер, значение числа Фибоначчи)