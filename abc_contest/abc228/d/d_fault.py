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
N = 2 ** 20 # 10 ** 6くらい


if __name__ == "__main__":
    Q = int(readline())
    order_manger = {}
    mod_manager = {}
    for i in range(Q):
        t, x = list_readline()
        if t == 1:
            order = i + 1
            while True:
                if not order_manger.get(order) or order_manger.get(order) == -1:
                    order_manger[order] = x
                    break
                else:
                    i = order_manger[i+1] % N - 1
            print("order_manger", order_manger)  # debug
        else:
            order = x % N
            ans = order_manger.get(order)
            ans = ans if ans else -1
            print(ans)
