import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc_prime_fact(n):
    limit_n = int(n ** 0.5)
    prime_l = []
    for i in range(limit_n, 0, -1):
        if n % i == 0:
            prime_l.append(i)
            if i != (n // i):
                prime_l.append(n // i)
    prime_l.sort(reverse=True)
    return prime_l

def calc_greatest_cmn_divisor(f, s, t):
    min_num = min(f, s, t)
    prime_l = calc_prime_fact(min_num)
    for p in prime_l:
        if f % p == 0 and s % p == 0 and t % p == 0:
            return p
# 計算量的にアウト
if __name__ == "__main__":
    k = int(snput())
    gcd_sum = 0
    for i in range(1, k+1):
        for j in range(1, k+1):
            for z in range(1, k+1):
                gcd_sum += calc_greatest_cmn_divisor(i, j, z)
    print(gcd_sum)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
