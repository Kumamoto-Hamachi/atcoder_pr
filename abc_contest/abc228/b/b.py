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
    n, x = list_readline()
    a_list = list_readline()
    know_list = [0] * n
    know_list[x-1] = 1
    order = x
    while True:
        new_order = a_list[order-1]
        if know_list[new_order-1]:
            break
        know_list[new_order-1] = 1
        order = new_order
    print(sum(know_list))
