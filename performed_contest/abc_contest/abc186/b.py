import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    h, w = m_snput()
    b_sum = 0
    b_min = 101
    for i in range(h):
        tmp_list = list(m_snput())
        tmp_min = min(tmp_list)
        b_sum += sum(tmp_list)
        if b_min > tmp_min:
            b_min = tmp_min
    print(b_sum - (b_min * h * w))
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
