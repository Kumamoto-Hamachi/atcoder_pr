import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    x, n = m_snput()
    p_l = list(m_snput())
    i = 0
    while True:
        if (x - i) not in p_l:
            print(x - i)
            break
        elif (x + i) not in p_l:
            print(x + i)
            break
        i += 1
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
