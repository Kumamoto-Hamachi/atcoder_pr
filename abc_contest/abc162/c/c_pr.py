import sys
from math import gcd
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    k = int(snput())
    k_l = [0] * 201
    ans = 0
    #下二つに相当
    for a in range(1, k+1): # gcd(a, b)
        for b in range(1, k+1): # cに相当
            k_l[a] += gcd(a, b)

    # 上2つに相当
    for a in range(1, k+1):
        for b in range(1, k+1):
            g = gcd(a, b) # nに相当さらに言えばaにも相当
            ans += k_l[g] # (n, 1)(n, 2)(n, 3)... (n, k)
    print(ans)
    """
    ans = 0
    for a in range(1, k+1):
        for b in range(1, k+1):
            n = gcd(a, b)
            for c in range(1, k+1):
                ans += gcd(c, n)
    print(ans)
    """

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
