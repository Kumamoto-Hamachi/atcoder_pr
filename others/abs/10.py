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
    S = sreadline()
    S = S[::-1]
    pattern = ["eraser", "dreamer", "erase", "dream"]
    pattern = [p[::-1] for p in pattern]
    flag = True
    while flag:
        bef_len = len(S)
        for p in pattern:
            p_len = len(p)
            if S[:p_len] == p:
                S = S[p_len:]
        aft_len = len(S)
        if aft_len == bef_len:
            flag = False
    if S:
        print("NO")
    else:
        print("YES")
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
