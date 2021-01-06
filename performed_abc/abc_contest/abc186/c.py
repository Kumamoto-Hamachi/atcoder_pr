import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    ten_accept = []
    for i in range(1, n+1):
        if not "7" in str(i):
            if not "7" in oct(i):
                ten_accept.append(i)
    print(len(ten_accept))

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
