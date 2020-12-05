import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc_gcd(max_num, a_list):
    almost_gcd = 0
    max_count = 0
    for i in range(2, max_num + 1):
        gcd_count =0
        for a in a_list:
            if a % i == 0:
                gcd_count += 1
        if gcd_count >= max_count:
            max_count = gcd_count
            almost_gcd = i
    return almost_gcd


if __name__ == "__main__":
    n = int(snput())
    a_list = list(m_snput())
    max_num = max(a_list)
    almost_gcd = calc_gcd(max_num, a_list)
    print(almost_gcd)
