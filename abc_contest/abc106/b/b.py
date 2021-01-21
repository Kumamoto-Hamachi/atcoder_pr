import sys
import math
# readlines = sys.stdin.buffer.readlines
# map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
# map_readline = lambda: map(int, readline().split())
# sreadline = lambda: readline().decode("utf-8")
# read
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

# 約数列挙
def make_divisors(num):
    divisors = []
    num_limit = math.floor(num ** 0.5)
    for i in range(2, num_limit+1):
        if num % i == 0:
            divisors.append(i)
            quotient = num // i
            if quotient != i:
                divisors.append(quotient)
    return divisors

# 素因数分解 1
def prime_factorize(num):
    primes = []
    i = 2
    while num >= i:
        if num % i == 0:
            num /= i
            primes.append(i)
            i = 1
        i += 1
    return primes

# 素因数分解 2
def prime_factorize_in_dict(num):
    primes = {}
    i = 2
    while num >= i:
        if num % i == 0:
            num /= i
            primes.setdefault(i, 0)
            primes[i] += 1
            i = 1
        i += 1
    return primes

def calc(num):
    cnt = 0
    for i in range(1, num+1, 2):
        primes = prime_factorize_in_dict(i)
        tmp = 1
        for v in primes.values():
            tmp *= (v+1)
        if tmp == 8:
            cnt += 1
    return cnt

# 約数の個数の求め方
# 素因数分解
# 各素数の(累乗+1)を掛けていく
# 例えば2 ** 3, 3 ** 1なら2を0~3回使う,3を0~1回使うの場合を考えてそれを掛ける
if __name__ == "__main__":
    n = int(readline())
    cnt = calc(n)
    print(cnt)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
