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
    A = list(map_readline())
    B = list(map_readline())
    min_num = -1
    max_num = math.inf
    for i in range(N):
        tmp_min = min(A[i], B[i])
        tmp_max = max(A[i], B[i])
        min_num = tmp_min if tmp_min > min_num else min_num
        max_num = max_num if tmp_max > max_num else tmp_max
    ans = max_num - min_num + 1
    if ans <= 0:
        print(0)
    else:
        print(ans)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
