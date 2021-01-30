from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
# read
# snput = sys.stdin.buffer.readline
# m_snput = lambda: map(int, snput().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
A 0:06
B 0:20
C 0:33
D 0:49
E 1:11
F 1:38

# アテ勘で解いてしまった...解き直しすること
if __name__ == "__main__":
    N = int(readline())
    limit = 2 * N
    cnt = 0
    divisors = make_divisors(limit)
    divisors
    for n in divisors:
        tmp = (2 * N - (n ** 2) + n) % (2 * n)
        if tmp == 0:
            cnt += 1
            n //= 2
        else:
            n -= 1
    print(cnt)


    """
    input_str = sreadline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
