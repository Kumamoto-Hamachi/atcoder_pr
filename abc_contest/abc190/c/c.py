from pprint import pprint as pp
from collections import defaultdict
import sys
from copy import copy
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
# read
# snput = sys.stdin.buffer.readline
# m_snput = lambda: map(int, snput().split())

def all_check(cp_dish, conditions):
    cnt = 0
    for c_l in conditions:
        if cp_dish[c_l[0]-1] and cp_dish[c_l[1]-1]:
            cnt += 1
    return cnt

if __name__ == "__main__":
    N, M = map_readline()
    dish = [False] * N
    conditions = [None] * M
    for i in range(M):
        conditions[i] = list(map_readline())
    K = int(readline())
    choice = [None] * K
    all_pattern = 2 ** K
    max_cnt = 0
    order = 0
    for i in range(K):
        choice[i] = list(map_readline())
    for a in range(all_pattern):
        cp_dish = copy(dish)
        for b in range(K):
            if ((a >> b) & 1):
                cp_dish[choice[b][1]-1] = True
            else:
                cp_dish[choice[b][0]-1] = True
        tmp_cnt = all_check(cp_dish, conditions)
        max_cnt = max(max_cnt, tmp_cnt)
    print(max_cnt)



    """
    input_str = sreadline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
