import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    b_l = list(m_snput())
    bc_l = [0] * (n + 1)
    for i in b_l:
        bc_l[i] += 1
    count = sum([i * (i - 1) // 2 for i in bc_l])
    for i in b_l:
        print(count - (bc_l[i] - 1))
    """
    m * (m - 1) / 2 - ((m - 1) * (m - 2) / 2)
    = (m - 1)(m - m + 2) / 2
    = m - 1
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
