import sys
import math
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    N = int(readline())
    p_l = list(map_readline())
    cnt = 0
    min_num = math.inf
    for i in range(N):
        min_num = min(min_num, p_l[i])
        if min_num == p_l[i]:
            cnt += 1
    print(cnt)

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

