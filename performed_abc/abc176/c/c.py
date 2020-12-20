import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    a_list = list(m_snput())
    b_list = a_list[:]
    for i in range(1, n):
        b_list[i] = max(b_list[i-1], b_list[i])
    step_sum = 0
    for i in range(n):
        step_sum += (b_list[i] - a_list[i])
    print(step_sum)


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
