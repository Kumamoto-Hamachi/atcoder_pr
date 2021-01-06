import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    input_str = snput()
    if "7" in input_str:
        print("Yes")
    else:
        print("No")
    """
    input_num = int(snput())
    some_map = m_snput()
    """
