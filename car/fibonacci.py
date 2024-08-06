class Fibonacci:

    def __init__(self, num):
        self.max_num = num

    def __iter__(self):
        self.first_num = 0
        self.second_num = 1
        return self

    def __next__(self):
        fib = self.first_num
        if fib > self.max_num:
            raise StopIteration
        self.first_num, self.second_num = self.second_num, self.first_num + self.second_num
        return fib


for n in Fibonacci(100):
    print(n, end=' ')


n = Fibonacci(1000)
s = 1
