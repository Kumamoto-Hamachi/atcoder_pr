import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a, b = m_snput()
    diff = abs(a - b)
    if diff < 3:
        print("Yes")
    else:
        print("No")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
