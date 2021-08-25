import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


MAX_COST = sys.maxsize


def study(books, comprehension):
    for i, v in enumerate(books):
        comprehension[i] += v
    return comprehension


def is_test_pass(comprehension, x):
    for v in comprehension:
        if v < x:
            return False
    return True


if __name__ == "__main__":
    n, m, x = map_readline()
    library = [None] * n
    prices = [None] * n
    for i in range(n):
        book = list(map_readline())
        prices[i] = book[0]
        library[i] = book[1:]

    patterns = 2 ** n
    min_cost = MAX_COST
    for p in range(patterns):
        cost = 0
        comprehension = [0] * m
        for i in range(n):
            if (p >> i) & 1:
                cost += prices[i]
                study(library[i], comprehension)
        if is_test_pass(comprehension, x):
            min_cost = min(min_cost, cost)

    if min_cost == MAX_COST:
        print(-1)
    else:
        print(min_cost)
