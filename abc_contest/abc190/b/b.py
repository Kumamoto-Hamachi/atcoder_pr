from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
# read
# snput = sys.stdin.buffer.readline
# m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    N, S, D = map_readline()
    for _ in range(N):
        X, Y = map_readline()
        if X < S and Y > D:
            print("Yes")
            sys.exit()
    print("No")

    """
    input_str = sreadline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
