from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
import itertools

def calc(a_l):
    sum_num = sum(a_l)
    for i in range(3):
        if sum_num - (a_l[i] * 3) == 0:
            return True
    return False


if __name__ == "__main__":
    a_l = list(map_readline())
    if calc(a_l):
        print("Yes")
    else:
        print("No")
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
