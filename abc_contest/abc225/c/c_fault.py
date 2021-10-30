import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def list_readline(): return list(map_readline())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]


def make_top_left_idx_candidate(top_left):
    top_left_idxs = []
    for J in range(1, 8):
        tmp_I = (top_left - J) / 7 + 1
        if int(tmp_I) == tmp_I and tmp_I >= 1 and tmp_I <= 10 ** 4:
            top_left_idxs.append([int(tmp_I), J])
    return top_left_idxs


def exists(top_left_idxs, b_group):
    for til in top_left_idxs:
        if is_all_match(til, b_group):
            return True
    return False


def is_all_match(til, b_group):
    a, b = til
    for i, b_row in enumerate(b_group):
        for j, col in enumerate(b_row):
            if calc(a+i, b+j) != col:
                return False
    return True


def calc(I, J):
    return (I - 1) * 7 + J


# 7, 8, 9
if __name__ == "__main__":
    N, M = list_readline()
    b_group = [None] * N
    for i in range(N):
        b_group[i] = list_readline()
    top_left = b_group[0][0]
    top_left_idxs = make_top_left_idx_candidate(top_left)
    print("calc(10 ** 4, 6)", calc(10 ** 4, 6))  # debug
    if exists(top_left_idxs, b_group):
        print("Yes")
    else:
        print("No")
