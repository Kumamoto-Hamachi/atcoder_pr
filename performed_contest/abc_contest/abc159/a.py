import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, m = m_snput()
    count = (n * (n - 1) + m * (m - 1)) // 2
    print(count)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
