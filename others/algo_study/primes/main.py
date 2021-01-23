import sys
# readlines = sys.stdin.buffer.readlines
# map_readlines = lambda: map(int, readlines())
# readline = sys.stdin.buffer.readline
# map_readline = lambda: map(int, readline().split())
# sreadline = lambda: readline().decode("utf-8")
# read
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

"""
約数の個数求める
https://juken-mikata.net/how-to/mathematics/number-of-divisor.html
"""

# 約数全列挙
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


# 素因数分解 1 List good
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


# 素因数分解 2 not good
def prime_factorize(num):
    primes = []
    limit = math.floor(n ** 0.5)
    tmp = num
    print("limit", limit)  # debug
    for i in range(2, limit+1):
        if tmp % i == 0:
            while tmp % i == 0:
                tmp //= i
                primes.append(i)
    if tmp != 1:
        primes.append(tmp)
    if primes == []:
        primes.append(num)
    return primes

# 素因数分解 3 Dict
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

# 整数N以下の素数を全て発見(約数じゃないよ!) エラトステネスのふるい
https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9
def get_sieve_of_eratosthenes(num):
    primes = [2]
    limit = math.floor(num ** 0.5)
    data = [i + 1 for i in range(2, n, 2)]
    # print("data", data)  # debug
    while True:
        p = data[0]
        if limit <= p:
            return primes + data
        primes.append(p)
        data = [i for i in data if i % p != 0]

if __name__ == "__main__":
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
