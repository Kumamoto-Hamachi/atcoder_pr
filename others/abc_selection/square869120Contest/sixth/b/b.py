import sys
import math
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


def calc_time(entrance, exit, a_l, b_l, N):
    all_time_sum = 0
    for i in range(N):
        a, b = a_l[i], b_l[i]
        time_sum = (abs(a-entrance) + abs(a-b) + abs(b-exit))
        all_time_sum += time_sum
    return all_time_sum


if __name__ == "__main__":
    N = int(readline())
    a_l = [None] * N
    b_l = [None] * N
    for i in range(N):
        a, b = map_readline()
        a_l[i] = a
        b_l[i] = b
    a_l = sorted(a_l)
    b_l = sorted(b_l)
    if N % 2 == 1:
        order = N // 2
        median_a = a_l[order]
        median_b = b_l[order]
        entrance = min(median_a, median_b)
        exit = max(median_a, median_b)
        min_time = calc_time(entrance, exit, a_l, b_l, N)
    else:
        order1 = N // 2
        order2 = order1 + 1
        median_a_l = [a_l[order1], a_l[order2]]
        median_b_l = [b_l[order1], b_l[order2]]
        min_time = math.inf
        for a in range(2):
            for b in range(2):
                median_a = median_a_l[a]
                median_b = median_b_l[b]
                entrance = min(median_a, median_b)
                exit = max(median_a, median_b)
                tmp_time = calc_time(entrance, exit, a_l, b_l, N)
                min_time = min(min_time, tmp_time)
    print(min_time)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
