from itertools import permutations
import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()


# 111, 112, 113, 114, 115,,, 444
num_list = []


def get_num(cur, n, m):
    if len(cur) >= n:
        print("cur", cur)  # debug
        num_list.append(cur)
        return
    """
    last = 1
    if len(cur) >= 1:
        last = len(cur) - 1
    """
    for i in range(1, m+1):
        nex = cur
        nex += str(i)
        get_num(nex, n, m)


if __name__ == "__main__":
    n, m, q = map_readline()
    q_list = [None] * n
    for i in range(q):
        q_list[i] = list(map_readline())
    cur = ""
    get_num(cur, n, m)
