import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())


if __name__ == "__main__":
    n = int(snput())
    a_l = list(m_snput())
    a_d = {}
    for a in a_l:
        a_d.setdefault(a, 0)
        a_d[a] += 1
    q = int(snput())
    ans = sum(a_l)
    for _ in range(q):
        b, c = m_snput()
        b_count = a_d.get(b) or 0
        c_count = a_d.get(c) or 0
        ans += (c * b_count - b * b_count)
        a_d[c] = b_count + c_count
        a_d[b] = 0
        print(ans)


    """TLEになる
    n = int(snput())
    a_s = snput()
    q = int(snput())
    change_d = {}
    for i in range(q):
        b, c = snput().split()
        a_s = a_s.replace(b, c)
        ans = sum(map(int, a_s.split(" ")))
        print(ans)
    """

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
