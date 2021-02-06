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
    v, t, s, d = map_readline()
    if v * t <= d and  d <= v * s:
        print("No")
    else:
        print("Yes")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
