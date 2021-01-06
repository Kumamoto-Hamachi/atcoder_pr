import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a, b, c, k = m_snput()
    if a >= k:
        print(1 * k)
    elif a + b >= k:
        print(1 * a)
    else:
        print(1 * a + (k - a - b) * -1)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
