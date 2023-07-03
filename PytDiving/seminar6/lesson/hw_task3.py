# 3. Напишите функцию в шахматный модуль. Используйте генератор случайных
#  чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный
#  случайные варианты и выведите 4 успешных расстановки.


from package import print_position, desk_check_beating, generate_random_position

number_true_pos = 4
cur_true_pos = 0

while cur_true_pos <= number_true_pos:
    position = generate_random_position()
    if desk_check_beating(position):
        print_position(position)
        cur_true_pos += 1

# position = [1, 5, 8, 6, 3, 7, 2, 4]  #позиция когда не бьют друг друга
# position = [5, 7, 8, 6, 3, 1, 2, 4]  # позиция когда бьют друг друга
# print_position(position)
# if desk_check_beating(position):
#     print('Ферзи бьют друг друга')
# else:
#     print('Ферзи НЕ бьют друг друга')
