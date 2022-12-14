# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# in
# 10 True
#
# out
#
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']
#
# in
# 10 False
#
# out
#
# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']

from random import choice, sample


def CreateJokes(nouns, adverbs, adjectives, jokes_count: int, uniq=False):
    jokes = []
    # вычисляем генерируемое количество шуток (сравнивая указанное кол-во шуток с минимальной длиной списка)

    if uniq == True:
        # из-за уникальности корректируем количество шуток, если требуется
        # (длина одного из списков меньше требуемого количества)
        min_len = len(nouns)
        if min_len > len(adverbs):
            min_len = len(adverbs)
        if min_len > len(adjectives):
            min_len = len(adjectives)
        if jokes_count > min_len:
            jokes_count = min_len
        # делаем уникальные выборки внутри списков
        nouns = sample(nouns, jokes_count)
        adverbs = sample(adverbs, jokes_count)
        adjectives = sample(adjectives, jokes_count)
        # объединяем выборки в список кортежей с помощью функции zip()
        tmp_ls = zip(nouns, adverbs, adjectives)
        for cur_tuple in tmp_ls:
            # объединяем кортеж в строку через пробел и помещаем в итоговый список шуток
            jokes.append(" ".join(cur_tuple))
    else:
        for i in range(jokes_count):
            # формируем список, взяв случайное значение из каждого исходного списка
            tmp_ls = [choice(nouns), choice(adverbs), choice(adjectives)]
            # объединяем список в строку через пробел и помещаем в итоговый список шуток
            jokes.append(" ".join(tmp_ls))
    return jokes, jokes_count


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
N = int(input('Укажите количество шуток: '))

res_ls, res_count = CreateJokes(nouns, adverbs, adjectives, N, True)
print(f'Шутки из уникальных слов - {res_count}: ')
print(res_ls)

res_ls, res_count = CreateJokes(nouns, adverbs, adjectives, N)
print(f'Шутки из неуникальных слов - {res_count}:')
print(res_ls)

# ['автомобиль когда-то яркий', 'лес завтра веселый', 'дом ночью зеленый', 'город вчера утопичный', 'огонь позавчера мягкий']
# Шутки из неуникальных слов - 10:
# ['город где-то яркий', 'город позавчера утопичный', 'автомобиль где-то яркий', 'автомобиль где-то веселый', 'лес сегодня мягкий', 'город где-то зеленый', 'город завтра веселый', 'автомобиль ночью веселый', 'лес вчера яркий', 'лес завтра зеленый']
