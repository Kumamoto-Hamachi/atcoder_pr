import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# もう少し綺麗な解き方ないか考える
if __name__ == "__main__":
    n, m = m_snput()
    h_list = list(m_snput())
    n_list = [True] * n
    for i in range(m):
        a, b = m_snput()
        ha, hb = h_list[a-1], h_list[b-1]
        if ha == hb:
            n_list[a-1], n_list[b-1] = False, False
        else:
            bad_ob = a if ha < hb else b
            n_list[bad_ob-1] = False
    print(sum(n_list))

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
