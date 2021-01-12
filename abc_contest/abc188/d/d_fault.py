import sys
from copy import copy
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def add(num , plus):
    return num + plus

if __name__ == "__main__":
    N, C = m_snput()
    all_s_l = [None] * N
    day_l = [0] * (10 *+ 9 + 1)
    print("day_l", day_l)  # debug
    first_day = 10 ** 9 + 1
    final_day = 0
    for i in range(N):
        a, b, c = list(m_snput())
        first_day = min(first_day, a)
        final_day = max(final_day, b)
        # day_l[a:b+1] = [c] * (b-a+1)
        tmp = list(map(add, day_l[a:b+1], [c] * (b-a+1)))
        day_l[a:b+1] = tmp
    # print("first_day, final_day", first_day, final_day)  # debug
    for i in range(first_day, final_day+1):
        day_l[i] = min(day_l[i], C)
    ans = sum(day_l)
    print(ans)

    """

    hoge = [0] * 3
    # hoge[1:2+1] += [1] * (2-1+1)
    fuga = list(map(add, hoge[1:2+1], [1] * (2-1+1)))
    hoge[1:2+1] = fuga
    print(hoge)

    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
