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
    all_contest = ["ABC", "ARC", "AGC", "AHC"]
    s_3 = [None] * 3
    for i in range(3):
        s_3[i] = sreadline()
    for i in range(4):
        if all_contest[i] not in s_3:
            print(all_contest[i])
            sys.exit()
