import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a_list = list(m_snput())
    print(min(a_list))
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
