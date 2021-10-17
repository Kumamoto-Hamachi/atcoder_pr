from pprint import pprint as pp
from collections import defaultdict
from itertools import permutations
import sys
import math
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def list_readline(): return list(map_readline())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]


if __name__ == "__main__":
    S = sreadline()
    s_len = len(S)
    min_S = S
    max_S = S
    for i in range(s_len):
        tmp = S[i:] + S[:i-s_len]
        min_S = min(min_S, tmp)
        max_S = max(max_S, tmp)
    print(min_S)
    print(max_S)
