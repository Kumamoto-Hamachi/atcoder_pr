import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, k = m_snput()
    n -= (n // k) * k
    n = min(n, abs(n - k))
    print(n)
    """
    0まで近づける
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
