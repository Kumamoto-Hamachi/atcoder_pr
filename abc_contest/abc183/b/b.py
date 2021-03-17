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
    sx, sy, gx, gy = map_readline()
    # ans = (gx - sx) / (sy + gy) * sy + sx
    # 鏡像を作ってやる、内分点/外分点の公式の考え方
    ans = (gx * sy + gy * sx) / (gy + sy)
    print(ans)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """

