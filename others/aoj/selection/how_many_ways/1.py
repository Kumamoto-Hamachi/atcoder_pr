from pprint import pprint as pp
import sys
import itertools
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def count_com_sum_is_specified_num(combinations, specified_num):
    cnt = 0
    for c in combinations:
        if sum(c) == specified_num:
            cnt += 1
    return cnt


if __name__ == "__main__":
    while True:
        n, p = map_readline()
        if n == 0 and p == 0:
            break
        n_l = (i for i in range(1, n+1))
        combinations = list(itertools.combinations(n_l, 3))
        cnt = count_com_sum_is_specified_num(combinations, p)
        print(cnt)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
