import sys
# readlines = sys.stdin.buffer.readlines
# map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
# map_readline = lambda: map(int, readline().split())
# sreadline = lambda: readline().decode("utf-8")
# read
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())


def factorize_prime(num):
    primes = {}
    i = 2
    while num >= i:
        if num % i == 0:
            num //= i
            primes.setdefault(i, 0)
            primes[i] += 1
            i = 1
        i += 1
    return primes


def count_divisors(prime_dict):
    divisor_num = 1
    for v in prime_dict.values():
        divisor_num *= (v+1)
    return divisor_num


if __name__ == "__main__":
    n = int(readline())
    cnt = 0
    for i in range(105, n+1, 2):  # 問題文の条件より105が最初の約数8個の奇数、奇数のみ確認
        primes = factorize_prime(i)
        if count_divisors(primes) == 8:
            cnt += 1
    print(cnt)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
