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


def find_idx(n, time_list, target):
    l_time = 0
    r_time = 0
    l_flg = True
    r_flg = True
    for i in range(n):
        l_time += time_list[i]
        if l_time == target: # JUST
            l_idx = i
            rest_time = 0
            return l_idx, rest_time
        elif l_time > target: # あとで
            if i == 0:
                rest_time = target
                l_idx = i - 1
            else:
                rest_time = target - (l_time - time_list[i])
                l_idx = i - 1
            return l_idx, rest_time


if __name__ == "__main__":
    n = int(readline())
    fuses = [None] * n
    max_time = 0
    time_list = [None] * n
    accumulate_len = [None] * n
    bef = 0
    for i in range(n):
        fuses[i] = list_readline() # 長さ, 速さ
        time_list[i] = fuses[i][0] / fuses[i][1]
        max_time += time_list[i]
        accumulate_len[i] = fuses[i][0] + bef
        bef = accumulate_len[i]
    ans_time = max_time / 2
    l_idx, rest_time = find_idx(n, time_list, ans_time)
    #print("rest_time", rest_time)  # debug
    #print("l_idx", l_idx)  # debug
    #print("accumulate_len", accumulate_len)  # debug
    if rest_time == 0:
        print(accumulate_len[l_idx])
    else:
        ans = 0
        if l_idx >= 0:
            ans += accumulate_len[l_idx]
        ans += fuses[l_idx+1][1] * rest_time
        print(ans)
