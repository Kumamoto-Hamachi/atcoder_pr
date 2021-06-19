from pprint import pprint as pp
from collections import defaultdict
from copy import copy
import sys
import math
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
sreadlines = lambda: [s.decode("utf-8").rstrip() for s in readlines()] # return strs per line list




if __name__ == "__main__":
    N = int(readline())
    a_l = list(map_readline())
    u_d = {}
    min_d = {}
    for i, a in enumerate(a_l):
        if u_d.get(a) is None:
            u_d[a] = (N - i - 1)
        else:
            u_d[a] += (N - i - 1)
            min_d.setdefault(a, 0)
            min_d[a] += 1
    ans = 0
    for v in u_d.values():
        ans += v
    for v in min_d.values():
        for vi in range(1, v+1):
            ans -= vi
    print(ans)

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    low_english_literature = " ".join(sreadlines())
    """
