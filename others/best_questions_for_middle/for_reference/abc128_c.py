import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


def is_all_light(idx, conditions, p_list):
    for i, condition in enumerate(conditions):
        switch = 0
        for sw_idx in condition[1:]:
            switch += (idx >> sw_idx - 1) & 1
        if switch % 2 != p_list[i]:
            return False
    return True


if __name__ == "__main__":
    N, M = map_readline()
    conditions = [None] * M
    for i in range(M):
        conditions[i] = list(map_readline())
    p_list = list(map_readline())

    cnt = 0
    patterns = 2 ** N
    for i in range(patterns):
        if is_all_light(i, conditions, p_list):
            cnt += 1
    print(cnt)
