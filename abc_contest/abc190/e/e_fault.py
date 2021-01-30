from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    N, M = map_readline()
    conditions = [None] * M
    n_l = [False] * (N + 1)
    for i in range(M):
        conditions[i] = list(map_readline())
    for c in conditions:
        n_l[c[0]] = True
        n_l[c[1]] = True
    print("n_l", n_l)  # debug
    K = int(readline())
    c_l = list(map_readline())
    for c in c_l:
        if not n_l[c]:
            print(-1)
            sys.exit()
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
