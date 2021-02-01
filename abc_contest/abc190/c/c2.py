import sys
from copy import copy
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def count_satisfied_conditions(conditions, dish):
    cnt = 0
    for c in conditions:
        if dish[c[0]] and dish[c[1]]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    N, M = map_readline()
    conditions = [None] * M
    for i in range(M):
        conditions[i] = list(map_readline())
    K = int(readline())
    patterns = 2 ** K
    trials = [None] * K
    for i in range(K):
        trials[i] = list(map_readline())
    max_cnt = 0
    for p in range(patterns):
        dish = [False] * (N + 1)
        for digit in range(K):
            trial = trials[digit]
            if (p >> digit) & 1:
                dish[trial[1]] = True
            else:
                dish[trial[0]] = True
        tmp_cnt = count_satisfied_conditions(conditions, dish)
        max_cnt = max(max_cnt, tmp_cnt)
    print(max_cnt)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
