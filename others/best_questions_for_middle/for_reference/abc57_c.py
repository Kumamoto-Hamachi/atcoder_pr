import sys
import math
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


if __name__ == "__main__":
    n = int(readline())
    limit_num = int(math.ceil(n ** 0.5))
    min_digits = sys.maxsize
    for i in range(1, limit_num+1):
        if n % i == 0:
            quotient = n // i
            digits = max(len(str(i)), len(str(quotient)))
            min_digits = min(min_digits, digits)
    print(min_digits)
