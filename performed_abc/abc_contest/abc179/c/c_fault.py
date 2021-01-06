import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def count_prime(a_b, a_b_max):
    count = 0
    for i in range(1, a_b_max+1):
        if a_b % i == 0:
            count += 1
            if a_b // i != i:
                count += 1
    return count

# TLE A * B <= N -1 O(N log N) バカ正直に素数を求める必要はないのでは？
if __name__ == "__main__":
    n = int(snput())
    abc_count = 0
    for i in range(1, n):
        a_b = n - i
        a_b_max = math.floor(a_b ** 0.5)
        abc_count += count_prime(a_b, a_b_max)
    print(abc_count)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
