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
    weathers = sreadline()
    w_l = weathers.split("S")
    ans = max([len(r) for r in w_l])
    print(ans)
    """
    weather_records = sreadline()
    if "RRR" in weather_records:
        print(3)
    elif "RR" in weather_records:
        print(2)
    elif "R" in weather_records:
        print(1)
    else:
        print(0)
    """
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """

