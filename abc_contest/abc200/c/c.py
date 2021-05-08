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

def calc(num):
    tmp = 0
    for i in range(1, num):
        tmp += i
    return tmp


if __name__ == "__main__":
    N = int(readline())
    a_l = list(map_readline())
    a_l = [i % 200 for i in a_l] # 2 * 10 ** 5
    a_d = {}
    for a in a_l:
        a_d.setdefault(a, 0)
        a_d[a] += 1
    #print("a_d", a_d)  # debug
    cnt = 0
    for v in a_d.values():
        cnt += calc(v)
    print(cnt)

    """
    order_l = list(range(N))
    combination_l = list(itertools.combinations(order_l, 2))
    cnt = 0
    for c in combination_l:
        num = a_l[c[0]] - a_l[c[1]]
        cnt += (num % 200 == 0)
    print(cnt)
    #"""
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
