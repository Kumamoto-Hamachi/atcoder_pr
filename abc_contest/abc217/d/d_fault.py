from itertools import permutations
from heapq import heappush, heappop
import sys
import math
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def list_readline(): return list(map_readline())
def sreadline(): return readline().decode("utf-8").rstrip()


def get_length(point, hp, L):
    left = None
    right = None
    min_left = sys.maxsize
    min_right = sys.maxsize
    for l in hp:
        if l[0] < point: # 左側はあった
            if min_left > (point - l[0]):
                min_left = point - l[0]
                left = l
        elif point < l[0]: # 右側はあった
            if min_right > (l[0] - point):
                min_right = l[0] - point
                right = l
    length = 0
    #print("left, right", left, right, L)  # debug
    if left is not None:
        length += left[1] # 左側の右
    else:
        length += L
        #print("length", length)  # debug
    if right is not None:
        length -= right[1] # 左側の右
    return length


if __name__ == "__main__":
    L, Q = map_readline()
    #l_list = [[2, 4, 1], [1, 3, 5]]
    hp = []
    for i in range(Q):
        query = list_readline()
        #print("query", query)  # debug
        if query[0] == 1: # 切る
            heappush(hp, [query[1], L-query[1]])
            #hp.append([query[1], L-query[1]]) # left, right
            #print("hp", hp)  # debug
        else: # 吐く
            length = get_length(query[1], hp, L)
            print(length)
            #print("ans", length)  # debug
