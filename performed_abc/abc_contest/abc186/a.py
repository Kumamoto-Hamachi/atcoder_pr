import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, w = m_snput()
    print(n // w)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
