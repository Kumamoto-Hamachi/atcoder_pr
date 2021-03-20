from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    n = int(readline())
    doublet_cnt = 0
    for _ in range(n):
        d1, d2 = map_readline()
        if d1 == d2:
            doublet_cnt += 1
            if doublet_cnt == 3:
                print("Yes")
                sys.exit()
        else:
            doublet_cnt = 0
    print("No")
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
