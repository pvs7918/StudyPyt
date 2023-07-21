# Для того, чтобы объект стал итерируемым, ему необходимо вернуть
# объект-итератор. В нашем случае экземпляр класса и есть объект-итератор.
# Следовательно он должен вернуть сам себя. Для возврата итератора нужно создать
# дандер метод __iter__.


class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.first < self.stop:
            self.first, self.second = self.second, self.first + \
                                      self.second
            if self.start <= self.first < self.stop:
                return self.first
        raise StopIteration

fib = Fibonacci(20, 100)
for num in fib:
    print(num)