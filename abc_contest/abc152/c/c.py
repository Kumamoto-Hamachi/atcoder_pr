import sys
import math
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    N = int(readline())
    p_l = list(map_readline())
    min_num = math.inf
    cnt = 0
    for p in p_l:
        min_num = min(min_num, p)
        if min_num == p:
            cnt += 1
    print(cnt)


    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

