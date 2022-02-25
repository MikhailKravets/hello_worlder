
class MyNumbers:

    def __init__(self):
        self.a = 0

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1

        if self.a == 11:
            raise StopIteration

        return x


def f(a, *, c=1, d=6, n):  # * means any kwarg after it
    return a, c, d, n


def g(a: float, b: float, /, c: float = 0):
    return a * b * c


if __name__ == '__main__':
    m = MyNumbers()

    for v in m:
        print(v)

    print(f(2, c=2, n=4, d=3))
    print(g(3, 3, c=1))
    print(42)
