from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


def f(N):
    N = list(str(N))
    N = sorted(N)
    big = int("".join(N[::-1]))
    small = int("".join(N))
    tmp = big - small
    return tmp


if __name__ == "__main__":
    N, K = map_readline()
    for i in range(K):
        N = f(N)
    print(N)
    """
    g1 大きい
    g2 小きい
    f = g1 - g2
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
