import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    x, y, z = m_snput()
    a, b, c = x, y, z
    a, b = b, a
    a, c = c, a
    print(a, b, c)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
