# # 1. В модуль с проверкой даты добавьте возможность запуска в терминале
# # с передачей даты на проверку.

import sys
from package import test_dates_argv

print('Привет, давай проверим даты!')
test_dates_argv()

# запустите в консоли:
# python hw_task1.py '25.06.1980' '25.06.1984'