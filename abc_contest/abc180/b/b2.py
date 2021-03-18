from pprint import pprint as pp
from collections import defaultdict
import sys
import math
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    n = int(readline())
    x_l = list(map_readline())
    max_abs = -1
    manhattan_distance = 0
    euclid_distance = 0
    for x in x_l:
        abs_x = abs(x)
        max_abs = max(max_abs, abs_x)
        manhattan_distance += abs_x
        euclid_distance += abs_x ** 2
    print(manhattan_distance)
    print(math.sqrt(euclid_distance))
    print(max_abs)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
