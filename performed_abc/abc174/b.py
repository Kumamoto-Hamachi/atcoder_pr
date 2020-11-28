import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc_distance_from_origin(limit_d):
    p, q = m_snput()
    d = math.sqrt(p ** 2 + q ** 2)
    if limit_d >= d:
        return True
    return False

if __name__ == "__main__":
    n, d = m_snput()
    count = 0
    for i in range(n):
        count += calc_distance_from_origin(d)
    print(count)
