import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


def calc_buying_time(n, doorway_idx, a_list, b_list):
    enter = a_list[doorway_idx-1]
    exit = b_list[doorway_idx-1]
    time = 0
    for i in range(n):
        a, b = a_list[i], b_list[i]
        time += abs(a - enter) + abs(b - a) + abs(exit - b)
    return time


if __name__ == "__main__":
    n = int(readline())
    a_list = [None] * n
    b_list = [None] * n
    for i in range(n):
        a, b = map_readline()
        a_list[i] = a
        b_list[i] = b
    a_list = sorted(a_list)
    b_list = sorted(b_list)
    if n % 2 == 1:
        doorway_idx = n // 2 + 1
        doorway_idx_list = [doorway_idx]
    else:
        doorway_idx1 = n // 2
        doorway_idx2 = n // 2 + 1
        doorway_idx_list = [doorway_idx1, doorway_idx2]

    min_ans = sys.maxsize
    for doorway_idx in doorway_idx_list:
        ans = calc_buying_time(n, doorway_idx, a_list, b_list)
        min_ans = min(min_ans, ans)
    print(min_ans)
