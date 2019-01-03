def nextCollatz(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n) + 1



def simCollatz(n: int) -> (int):
    yield n
    while n != 4:
        n = nextCollatz(n)
        yield n
    yield 2
    yield 1


print([x for x in simCollatz(10)])