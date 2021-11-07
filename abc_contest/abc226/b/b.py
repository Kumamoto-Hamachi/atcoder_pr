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
    N = int(readline())
    count_dict = {}
    for _ in range(N):
        num_list = tuple(list_readline())
        count_dict.setdefault(num_list, 0)
        count_dict[num_list] += 1
    count = len(count_dict)
    print(count)
