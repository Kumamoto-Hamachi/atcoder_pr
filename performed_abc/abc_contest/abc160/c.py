import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    k, n = m_snput()
    a_list = list(m_snput())
    # a_list.extend([0, k])
    a_list.append(k)
    a_list.sort()
    # print("a_list", a_list)  # debug
    a_len = len(a_list)
    diff_l = [None] * (a_len - 1)
    for i in range(a_len-1):
        diff_l[i] = a_list[i+1] - a_list[i]
        if i == a_len - 2:
            diff_l[i] += a_list[0]
    # print("diff_l", diff_l)  # debug
    ans = sum(diff_l) - max(diff_l)
    print(ans)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
