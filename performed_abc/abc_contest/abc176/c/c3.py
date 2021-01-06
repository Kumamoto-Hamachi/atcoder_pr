import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# この書き方が現状一番早い？
if __name__ == "__main__":
    n = int(snput())
    a_list = list(m_snput())
    step_sum = 0
    tmp = a_list[0]
    for i in a_list[1:]:
        if tmp > i:
            step_sum += (tmp - i)
        else:
            tmp = i
    print(step_sum)


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
