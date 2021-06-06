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
    N = int(readline())
    a_l = list(map_readline())
    kinomi = 0
    for a in a_l:
        if a > 10:
            kinomi += (a - 10)
    print(kinomi)
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
    N = int(readline())
    a_l = list(map_readline())
    kinomi = 0
    for a in a_l:
        if a > 10:
            kinomi += (a - 10)
    print(kinomi)
