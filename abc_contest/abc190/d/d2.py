import sys
import math
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def make_divisors(num):
    divisors = []
    limit = math.floor(num ** 0.5)
    for i in range(1, limit+1):
        if num % i == 0:
            divisors.append(i)
            quotient = num // i
            if quotient != i:
                divisors.append(quotient)
    return divisors


if __name__ == "__main__":
    N = int(readline())
    divisors = make_divisors(N)
    cnt = 0
    for d in divisors:
        if d % 2 == 1:
            cnt += 1
    print(cnt * 2) # 項数が奇数の時とvalue(真ん中 or 真ん中付近2つの合計)が奇数の時の2パターン
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
