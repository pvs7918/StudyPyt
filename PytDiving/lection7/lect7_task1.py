# open(file, mode='r', buffering=-1, encoding=None, errors=None,
#     newline=None, closefd=True, opener=None)
#
# f = open('text_data.txt')
# print(f)
# print(list(f))
#
# f = open('text_data.txt', 'r', encoding='utf-8')
#
# режимы работы с файлами.
# ➢ 'r' — открыть для чтения (по умолчанию)
# ➢ 'w' — открыть для записи, предварительно очистив файл
# ➢ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже
# существует
# ➢ 'a' — открыть для записи в конец файла, если он существует
# ➢ 'b' — двоичный режим
# ➢ 't' — текстовый режим (по умолчанию)
# ➢ '+' — открыты для обновления (чтение и запись)

# f = open('text_data.txt', 'a', encoding='utf-8')
# f.write('Окончание файла\n')
# f.close()   #Закрытие файла гарантирует сохранение информации на носителе.


# Работа с бинарными файлами
# f = open('bin_data', 'wb', buffering=64)
# f.write(b'X' * 1200)
# f.close()

# f = open('data.txt', 'wb')
# f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
# f.close()
# f = open('data.txt', 'r', encoding='utf-8')
# print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode
# byte 0xec in position 14: invalid continuation byte
# f.close()
# f = open('data.txt', 'r', encoding='utf-8', errors='replace')
# print(list(f))
# f.close()

#Использование менеджера контекста with, чтобы избежать ошибок закрытия файла.
# with open('text_data.txt', 'r+', encoding='utf-8') as f:
# print(list(f))
# print(f.write('Пока'))

#менеджер контекста позволяет одновременно открыть несколько файлов
# with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
# open('bin_data', 'rb') as f2, \
# open('data.txt', 'r', encoding='utf-8',
# errors='backslashreplace') as f3:
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# # Начиная с Python 3.10 менеджер контекста поддерживает круглые скобки для
# # группировки нескольких операторов по строкам:
# with (open('text_data.txt', 'r+', encoding='utf-8') as f1,
# open('bin_data', 'rb') as f2,
# open('data.txt', 'r', encoding='utf-8',
# errors='backslashreplace') as f3):
#
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))
#
# # Чтение файла в список.
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#         print(list(f))
#
# with open('text_data.txt', 'r', encoding='utf-8') as f:
# res = f.read()
# print(f'Читаем первый раз\n{res}')
# # повторное чтение возвращает пустую строку
# res = f.read()
# print(f'Читаем второй раз\n{res}')
#
# # построчное чтение файла
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.readline():
#         print(res)

# Вместо метода readline без аргумента можно использовать более короткую запись с циклом for
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')

# Символ переноса строки сохранился в конце каждой строки.
# Если вам необходимо обработать строку без переносов, можно использовать
# срезы line[:-1] или метод замены line.replace('\n', '')

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line[:-1])
#         print(line.replace('\n', ''))

#                   Запись и добавление в файл

# С режимами записи мы уже познакомились.
# ➢ w — создаём новый пустой файл для записи. Если файл существует,
# открываем его для записи и удаляем данные, которые в нём хранились.
# ➢ x — создаём новый пустой файл для записи. Если файл существует, вызываем
# ошибку.
# ➢ a — открываем существующий файл для записи в конец, добавления данных.
# Если файл не существует, создаём новый файл и записываем в него.

# text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     res = f.write(text)
#     print(f'{res = }\n{len(text) = }')

# Если каждая строка должна сохранятся в файле с новой строки, необходимо
# самостоятельно добавить символ переноса - \n

# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
# 'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
# 'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')
#         print(f'{res = }\n{len(line) = }')
#
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     f.writelines('\n'.join(text))

# Функция print по умолчанию выводит информацию в поток вывода. Обычно это
# консоль. Но можно явно передать файловый объект для печати в файл. Для этого
# надо воспользоваться ключевым параметром file.
#
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#   for line in text:
#       print(line, file=f)

# В отличии от методов записи в файл, функция print добавляет перенос строки.
# Кроме того ничто не мешает явно изменить параметр end функции.
#
# with open('new_data.txt', 'a', encoding='utf-8') as f:
# for line in text:
# print(line, end='***\n##', file=f)

#                       Методы перемещения в файле
# Метод tell возвращает текущую позицию в файле.

# Метод seek позволяет изменить положение “курсора” в файле.
# seek(offset, whence=0), где offset — смещение относительно опорной точки, whence -
# способ выбора опороной точки.
# ● whence = 0 - отсчёт от начала файла
# ● whence = 1 - отсчёт от текущей позиции в файле
# ● whence = 2 - отсчёт от конца файла
# 🔥 Важно! Значения 1 и 2 допустимы только для работы с бинарными
# файлами. Исключение seek(0, 2) для перехода в конец текстового файла.

# truncate(size) - изменить размер файла до указанного

                            # Файловая система
# Текущий каталог
# Для получения информации о текущем каталоге можно использовать модуль os или
# pathlib
# import os
# from pathlib import Path
# print(os.getcwd())
# print(Path.cwd())

# os.chdir('../..')

# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()

# Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)   # создать недостающие подкаталоги

# Удаление каталогов
# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()

# Удаление каталогов с содержимым
# import shutil
# shutil.rmtree('dir/other_dir')
# shutil.rmtree('some_dir')

# Формирование названия пути
# import os
# from pathlib import Path
# file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
# print(f'{file_1 = }\n{file_1}')
# file_2 = Path().cwd() / 'dir' / 'new_file.txt'
# print(f'{file_2 = }\n{file_2}')
# Оба варианта используют разные способы получения результата и хранения
# информации. Но результат мы получили один и тот же — путь до файла new_file.txt в
# каталоге dir текущего каталога.

# Для получения информации о том какие директории и файлы находятся в текущем
# каталоге можно воспользоваться следующими вариантами кода.
# Функция listdir возвращает список файлов и каталогов. Метод iterdir у экземпляра
# класса Path является генератором. В цикле он возвращает объекты из выбранной
# директории.
#
# import os
# from pathlib import Path
# print(os.listdir())
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)

# Проверка на директорию, файл и ссылку
# Получив информацию о содержимом текущего каталога зачастую требуется
# уточнить что перед нами. В каталогах можно хранить другие каталоги и файлы. В
# файлах содержатся данные. А символьные ссылки указывают на каталоги и файлы
# из других мест.
#
# import os
# from pathlib import Path
# dir_list = os.listdir()
# for obj in dir_list:
#     print(f'{os.path.isdir(obj) = }', end='\t')
#     print(f'{os.path.isfile(obj) = }', end='\t')
#     print(f'{os.path.islink(obj) = }', end='\t')
#     print(f'{obj = }')
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(f'{obj.is_dir() = }', end='\t')
#     print(f'{obj.is_file() = }', end='\t')
#     print(f'{obj.is_symlink() = }', end='\t')
#     print(f'{obj = }')

# Обход папок через os.walk()
#
# import os
# for dir_path, dir_name, file_name in os.walk(os.getcwd()):
#     print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
# Функция возвращает кортеж из трёх значений:
# ➢ dir_path — абсолютный путь до каталога
# ➢ dir_names — список с названиями всех каталогов, находящихся в dir_path
# 20
# ➢ dir_names — список с названиями всех файлов, находящихся в dir_path
# Вывод продолжается до тех пор пока не будет возвращена информация обо всех
# директориях, т.е. каждая директория из dir_names передаётся в os.walk и
# оказывается в dir_path.

# Переименование файлов
# import os
# from pathlib import Path
# os.rename('old_name.py', 'new_name.py')
# p = Path('old_file.py')
# p.rename('new_file.py')
# Path('new_file.py').rename('newest_file.py')

# Перемещение файлов
# import os
# from pathlib import Path
# 21
# os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir',
# 'new_name.py'))
# old_file = Path('new_name.py')
# new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)
# Для исходного файла явно не указывали директорию, где он расположен. При
# переносе была указана текущая директория как отправная точка. Оба варианта
# имеют одинаковый эффект.

# Копирование файлов
# import shutil
# shutil.copy('one.txt', 'dir')
# shutil.copy2('two.txt', 'dir')


# Скопировать каталог со всем его содержимым в новое место,
# модуль предоставляет функции copytree.
# import shutil
# shutil.copytree('dir', 'one_more_dir')

# Удаление файлов
# import shutil
# 22
# shutil.rmtree('dir')

# Если же необходимо удалить один файл, можно воспользоваться следующими
# вариантами:
# import os
# from pathlib import Path
# os.remove('one_more_dir/one.txt')
# Path('one_more_dir/one_more.txt').unlink()

