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
    x, y = map_readline()
    if x == y:
        print(x)
    else:
        for i in range(3):
            if i not in ([x, y]):
                print(i)
                sys.exit()
