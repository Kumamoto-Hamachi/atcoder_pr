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
    s, t, x = list_readline()
    if s == x:
        print("Yes")
        sys.exit()
    while True:
        s += 1
        s = 0 if s == 24 else s
        if s == x and s != t:
            print("Yes")
            break
        elif s == t:
            print("No")
            break
