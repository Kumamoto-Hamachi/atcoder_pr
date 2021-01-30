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
    a, b, c = map_readline()
    if c == 0:
        if a == b:
            print("Aoki")
        elif a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a == b:
            print("Takahashi")
        elif a > b:
            print("Takahashi")
        else:
            print("Aoki")
    """
    input_str = sreadline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
