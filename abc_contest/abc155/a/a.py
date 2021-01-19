import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    three = m_snput()
    three_set = set(three)
    if len(three_set) == 2:
        print("Yes")
    else:
        print("No")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
