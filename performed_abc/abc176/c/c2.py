import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    a_list = list(m_snput())
    step_sum = 0
    for i in range(1, n):
        if a_list[i-1] > a_list[i]:
            step_sum += (a_list[i-1] - a_list[i])
            a_list[i] = a_list[i-1]
    print(step_sum)


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
