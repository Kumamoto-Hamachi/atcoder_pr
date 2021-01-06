import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, k = m_snput()
    f_list = list(m_snput())
    f_list.sort()
    sum_m = 0
    for i in range(k):
        sum_m += f_list[i]
    print(sum_m)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
