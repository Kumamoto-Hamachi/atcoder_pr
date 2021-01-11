import sys
from math import log
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def is_prime_num(num):
    max_try_num = int(num ** 0.5)
    for i in range(2, max_try_num):
        if num % i == 0:
            return False
    return True

def wa(first, r, n):
    ans = (first * r ** n - first) / (r -1)
    print(ans)


if __name__ == "__main__":
    k = int(snput())
    if k % 7 == 0:
        print(1)
        sys.exit()
    elif k == 2 or k == 5:
        print(-1)
        sys.exit()
    elif not is_prime_num(k):
        print(-1)
        sys.exit()
    value = 1
    order = log((9 * k + 1), 10)
    print("order", order)  # debug
    wa(1, 10, 999982)
    """
    while True:
        if value % k == 0:
            print(order)
            sys.exit()
        value += 10 ** (order)
        order += 1
    """

    """
    a(r ** n - 1) / (r-1) = k
    9k+1 = 10 ** n
    7 * 1111
    1 + 10 + 100 + 1000 +
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
