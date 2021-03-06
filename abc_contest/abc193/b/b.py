from pprint import pprint as pp
from collections import defaultdict
import sys
import math
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def is_there_machine(minute, machine_stock):
    minute = math.floor(minute + 0.5)
    if (machine_stock - minute) >= 1:
        return True
    return False

if __name__ == "__main__":
    N = int(readline())
    min_num = math.inf
    for _ in range(N):
        minute, price, machine_stock = map_readline()
        if is_there_machine(minute, machine_stock):
            min_num = min(min_num, price)
    if min_num < math.inf:
        print(min_num)
    else:
        print(-1)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
