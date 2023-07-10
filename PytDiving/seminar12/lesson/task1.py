# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

class Factorial:

    def __init__(self):
        self.results = defaultdict(list)

    def __call__(self, number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.results[number].append(result)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.results.items()))
        return txt


factor = Factorial()

factor(1)
factor(10)
factor(6)

print(factor)