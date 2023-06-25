# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

text = 'У нас все хорошо. А будет еще лучше!'

def every_word(text: str):
    text1 = text.lower().split()
    max_ = len(max(text1, key=len))
    text1.sort()
    for i, el in enumerate(text1, 1):
        print(f'{i} {el:>{max_}}')

every_word(text)