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
    n = int(readline())
    num_dict = {}
    for _ in range(n-1):
        f, s = list_readline()
        num_dict.setdefault(f, set())
        num_dict.setdefault(s, set())
        num_dict[f].add(s)
        num_dict[s].add(f)
    #print("num_dict", num_dict)  # debug
    for k, v_set in num_dict.items():
        if len(v_set) == n - 1:
            print("Yes")
            sys.exit()
    print("No")
