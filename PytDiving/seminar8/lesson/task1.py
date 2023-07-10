# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

import json

with open("task1.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

result_dict = {}
for line in lines:
    line = line.strip().split()  # strip удаляем символы в начале и в конце строки. по уомлчанию пробелы
    result_dict[line[0].title()] = line[1]  # метод title делает первую букву строки заглавной
# print(result_dict)

with open('task1_result.json', 'w', encoding='utf-8') as f:
    json.dump(result_dict, f, indent=4, ensure_ascii=False)
