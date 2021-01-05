import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    a_sum = 0
    s_sum = 0
    s_l = [None] * n
    for i in range(n):
        a, t = m_snput()
        a_sum += a
        s_sum = (2 * a + t)
        s_l[i] = s_sum
    s_l.sort(reverse=True)
    tmp = 0
    for i, s in enumerate(s_l):
        tmp += s
        if tmp > a_sum:
            print(i+1)
            sys.exit()

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
