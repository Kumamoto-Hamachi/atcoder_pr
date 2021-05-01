from pprint import pprint as pp
from collections import defaultdict
import sys
import math
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def calc_min_h(d, h, D, H):
    min_h = (H / D * d - h) * (D / (d - D))
    return min_h

if __name__ == "__main__":
    N, D, H = map_readline()
    disturbs = [None] * N
    min_h = 0
    for i in range(N):
        d, h = map_readline()
        tmp_h = calc_min_h(d, h, D, H)
        if tmp_h >= min_h:
            min_h = tmp_h
    print(min_h)

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
