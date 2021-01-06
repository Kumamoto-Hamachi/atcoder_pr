import sys
from math import gcd
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    k = int(snput())
    gcd_sum = [0] * 200 ** 3
    ans = 0

    for i in range(1, k+1):
        for j in range(1, k+1):
            gcd_sum[i] += gcd(i, j)

    for a in range(1, k+1):
        for b in range(1, k+1):
            g = gcd(a, b)
            ans += gcd_sum[g]
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
