from pprint import pprint as pp
from collections import defaultdict
import sys
import math
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]


if __name__ == "__main__":
    N = int(readline())
    limit_num = int(math.log2(N))
    limits = [limit_num -2, limit_num-1, limit_num, limit_num+1,limit_num+2]
    ans = 0
    for k in limits:
        if k < 0:
            continue
        if 2 ** k <= N:
            ans = k
    print(ans)


