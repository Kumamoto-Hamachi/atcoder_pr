import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# コードが汚すぎる
if __name__ == "__main__":
    n, m = m_snput()
    """
    if m == 0:
        print(0)
        sys.exit()
    """
    a_list = list(m_snput())
    a_list.append(0)
    a_list.append(n+1)
    a_list.sort()
    min_gap = 10 ** 19
    a_len = len(a_list)
    gap_l = [None] * (a_len - 1)
    # print("a_list", a_list)  # debug
    for i in range(a_len-1):
        tmp_gap = a_list[i+1] - a_list[i] - 1
        # print("tmp_gap", tmp_gap)  # debug
        gap_l[i] = tmp_gap
        if tmp_gap != 0:
            min_gap = min(tmp_gap, min_gap)
    # print("min_gap", min_gap)  # debug
    # print("gap_l", gap_l)  # debug
    count = 0
    for g in gap_l:
        count += -(-g // min_gap)
    print(count)


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
