import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    N, R = m_snput()
    print(R if N >= 10 else R + (100 * (10 - N)))
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
