from pprint import pprint as pp
from collections import defaultdict
import sys
import itertools
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    N = int(readline())
    a_l = list(map_readline())
    ans = 0
    a_sum = sum(a_l)
    for a in a_l:
        ans += (a ** 2) * (N-1)
        a_sum -= a
        ans -= a * a_sum * 2
    print(ans)

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
