import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    sum_n = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            sum_n += i
    print(sum_n)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
