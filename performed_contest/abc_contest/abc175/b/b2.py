import sys
import itertools
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    """
    if n < 3:
        print(0)
        sys.exit()
    """
    some_list = list(m_snput())
    some_list.sort()
    count = 0
    # some_listが2個しかないと動かないままで終わる
    for trio  in itertools.combinations(some_list, 3):
        a, b ,c = trio
        if (a + b) > c and c > abs(a - b) and (a != b) and (b != c) and (c != a):
            count += 1
    print(count)
