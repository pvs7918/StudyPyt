# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.

import logging
# logging.basicConfig(level=logging.NOTSET)
# logging.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
# logging.info('Немного информации о работе кода')
# logging.warning('Внимание! Надвигается буря!')
# logging.critical('На этом всё')


logging.basicConfig(filename='task1.log', filemode='w',
encoding='utf-8', level=logging.ERROR)

a, b = map(int, input("Введите a b: ").split())
try:
    c = a / b
    print(c)
except Exception as e:
    logging.warning(f'Возникла ошибка при делении. {e}')

