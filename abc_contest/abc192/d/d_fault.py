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


def Base_n_to_10(X,n):
    out = 0
    X_str = str(X)
    lens = len(X_str) + 1
    for i in range(1,lens):
        out += int(X_str[-i])*(n**(i-1))
    return out#int out


def hoge(X_num, M, d):
    flag = False
    while True:
        num = Base_n_to_10(X_num, d)
        if num <= M:
            d *= 2
            flag = True
        else:
            d //= 2
            return d, flag

if __name__ == "__main__":
    X = sreadline()
    X_num = int(X)
    M = int(readline())
    max_num = 0
    for x in X:
        max_num = max(max_num, int(x))
    d = max_num + 1
    kinds = 0
    M_str = str(M)
    while True:
        flag = True
        d, flag = hoge(X_num, M, d)
        if not flag:
            d *= 2
            break
        d += 1
    # print("d", d)  # debug
    print(d-max_num)
    """
    while True:
        num = int(Base_n_to_10(X_num, d))
        # print("num", num)  # debug
        if num >= M:
            d -= 1
        else:
            break
    print(d - max_num)
    """
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
