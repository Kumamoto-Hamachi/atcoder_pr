import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc_count(num, b_d):
    count = 0
    for k, v in b_d.items():
        if k == num:
            v -= 1
        if v >= 2:
            count += v * (v - 1) / 2
    return int(count)

if __name__ == "__main__":
    n = int(snput())
    b_l = list(m_snput())
    b_d = {}
    for b in b_l:
        b_d.setdefault(b, 0)
        b_d[b] += 1
    coutn_d = {}
    for i in range(n):
        num = b_l[i]
        if num not in coutn_d.keys():
            coutn_d[num] = calc_count(num, b_d)
        print(coutn_d[num])
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
