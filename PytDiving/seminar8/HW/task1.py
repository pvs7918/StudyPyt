# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# []
# ○Для дочерних объектов указывайте родительскую директорию.
# ○Для каждого объекта укажите файл это или директория.
# ○Для файлов сохраните его размер в байтах, а для директорий размер файлов в
# ней с учётом всех вложенных файлов и директорий.

import os
import csv
import json
import pickle


def read_folder(subfolder_name):
    # полной путь к сканируемому каталогу
    dir_name = os.path.join(os.getcwd(), subfolder_name)
    res_list = []  # результирующий список словарей

    # Обход подкаталогов и файлов с помощью os.walk
    for dir_path, dir_names, file_names in os.walk(dir_name):
        # получаем списки подкаталогов dir_name и файлов file_name
        for cur_dir in dir_names:
            dict_row = {}
            dict_row['parent_fold'] = dir_path
            dict_row['type'] = 'folder'
            dict_row['name'] = cur_dir
            dict_row['size'] = 0
            res_list.append(dict_row)

        for cur_file in file_names:
            dict_row = {}
            dict_row['parent_fold'] = dir_path
            dict_row['type'] = 'file'
            dict_row['name'] = cur_file
            dict_row['size'] = os.path.getsize(os.path.join(dir_path, cur_file))  # размер файла в байтах
            res_list.append(dict_row)

    # запись результирующего списка словарей в файл json
    with open('task1_res.json', 'w', encoding='utf-8') as f1:
        json.dump(res_list, f1, ensure_ascii=False, indent=4)
    # запись результирующего списка словарей в файл csv
    with open('task1_res.csv', 'w', newline='', encoding='utf-8') as f2:
        csv_write = csv.DictWriter(f2,
                                   fieldnames=["parent_fold", "type", "name", "size"],
                                   dialect='excel',
                                   quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(res_list)
    # запись результирующего списка словарей в файл pickle
    with open('task1_res.pickle', "wb") as f3:
        pickle.dump(res_list, f3)

if __name__ == "__main__":
    read_folder("Task1_Fold")
