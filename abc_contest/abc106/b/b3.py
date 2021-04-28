import sys
import math
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

def count_divisor(num):
    cnt = 0
    limit = math.ceil(num ** 0.5)
    for i in range(1, limit+1):
        if num % i == 0:
            cnt += 1
            if num // i != i:
                cnt += 1
    return cnt

if __name__ == "__main__":
    N = int(readline())
    target_cnt = 0
    for i in range(1, N+1, 2):
        divisor_cnt = count_divisor(i)
        target_cnt += 1 if divisor_cnt == 8 else 0
    print(target_cnt)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """

