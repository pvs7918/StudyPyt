# 📌Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# 📌возврат строки без изменений
# 📌возврат строки с преобразованием регистра без потери символов
# 📌возврат строки с удалением знаков пунктуации
# 📌возврат строки с удалением букв других алфавитов
# 📌возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
import doctest
from string import ascii_lowercase





def removal_chars(text: str) -> str:
    """
    >>> removal_chars("QWERTY") == "qwerty"
    True
    >>> removal_chars("QWER TY2") == "qwer ty"
    True
    """
    result = ''
    for ch in text.lower():
        if ch in ascii_lowercase + ' ':
            result += ch

    return result

if __name__ == "__main__":
    # print(removal_chars("QWER TY2"))
    doctest.testmod(verbose=True)       # запуск testmod - тестирование кода
