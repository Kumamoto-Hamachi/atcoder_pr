import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a, b = m_snput()
    for i in range(1, 1251):
        if i * 8 // 100 == a and i * 10 // 100 == b:
            print(i)
            sys.exit()
    print(-1)
    """
    x * 8 / 100 == 100
    x * 10 / 100 == 100
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
