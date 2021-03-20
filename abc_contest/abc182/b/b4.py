from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

# b3のほうが美しい書き方
if __name__ == "__main__":
    n = int(readline())
    a_l = list(map_readline())
    limit = max(a_l)
    ans, max_cnt = 0, 0
    for i in range(2, limit+1):
        cnt = len([a for a in a_l if a % i == 0])
        ans, max_cnt = (i, cnt) if cnt >= max_cnt else (ans, max_cnt)
    print(ans)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """

