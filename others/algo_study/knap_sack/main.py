from pprint import pprint as pp
from collections import defaultdict
import sys
from copy import copy
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def dp(w_v, item):
    weight = item[0]
    value = item[1]
    w_v[weight] += value
    tmp_w_v = copy(w_v)
    for i, v in enumerate(w_v):
        if v > 0:
            tmp_w_v[i+weight] = w_v[i] + value
            print("w_v", w_v, len(w_v))  # debug
    return w_v


if __name__ == "__main__":
    N = 5
    item_l = [None] * N
    w_sum = 0
    for i in range(N):
        item_l[i] = list(map_readline())
        w_sum += item_l[i][0]
    w_v = [0] * w_sum  # length express weight
    w_v[0] = 0
    for item in item_l:
        print("item", item)  # debug
        w_v = dp(w_v, item)
    print("w_v", w_v)  # debug
    max_v = 0
    opt_w = 0
    for i, v in enumerate(w_v[:10]):
        print("i, v", i, v)  # debug
        if v > max_v:
            max_v = v
            opt_w = i
    print("max_v, opt_w", max_v, opt_w)  # debug

    """
    幾つかの品物があり、この品物にはそれぞれ重量・価値の
    2つのパラメータが与えられています。
    ある一定の重さまで品物を運べるとしたときに、
    価値の合計の最大値は幾つになるでしょう？
    w, v
    a 3-2
    a 4-3
    a 3-2
    a 3-2
    a 3-2
    =>vを最大化,wを制限
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
