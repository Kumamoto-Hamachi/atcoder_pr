from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
sreadlines = lambda: [s.decode("utf-8").rstrip() for s in readlines()] # return strs per line list

if __name__ == "__main__":
    n = int(readline())
    a_l = list(map_readline())
    cnt = 0
    u_d = {}
    minus_d = {}
    for i, a in enumerate(a_l):
        if u_d.get(a) is None:
            u_d[a] = n - i - 1
        else:
            u_d[a] += n - i - 1
            minus_d.setdefault(a, 0)
            minus_d[a] += 1
    for v in u_d.values():
        cnt += v
    for v in minus_d.values():
        for i in range(1, v+1):
            cnt -= i
    print(cnt)
    """
    for i in range(n-1):
        for j in range(i+1, n):
            cnt += a_l[i] != a_l[j]
    """

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    low_english_literature = " ".join(sreadlines())
    """
