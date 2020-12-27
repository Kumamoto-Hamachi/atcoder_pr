import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    l = int(snput())
    t = l / 3
    l_max = t ** 3
    print(l_max)

    """
    v, s, h
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
