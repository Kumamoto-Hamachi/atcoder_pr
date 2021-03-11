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

if __name__ == "__main__":
    N = int(readline())
    a_l = [None] * N
    b_l = [None] * N
    total_min = math.inf
    tmp_min_a = math.inf
    tmp_min_b = math.inf
    for i in range(N):
        a, b = map_readline()
        total_min = min(a+b, total_min)
        a_l[i] = a
        b_l[i] = b
    for i in range(N):
        tmp = a_l[i]
        for j in range(N):
            if tmp <= b_l[j] and j != i:
                tmp_min_a = min(b_l[j], tmp_min_a)
    for i in range(N):
        tmp = b_l[i]
        for j in range(N):
            if tmp <= a_l[j] and j != i:
                tmp_min_b = min(a_l[j], tmp_min_b)
    ans = min(tmp_min_a, tmp_min_b, total_min)
    print(ans)




    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
