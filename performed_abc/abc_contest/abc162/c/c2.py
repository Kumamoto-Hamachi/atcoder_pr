import sys
from math import gcd
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    k = int(snput())
    gcd_sum = [0] * 201
    ans = 0

    for i in range(1, k+1):
        for j in range(1, k+1):
            num = gcd(i, j)
            for l in range(1, k+1):
                ans += gcd(num, l)
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
