import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a, b, c, d = m_snput()
    result = "No"
    while a > 0 and c > 0:
        if result == "No":
            c -= b
            result = "Yes"
        elif result == "Yes":
            a -= d
            result = "No"
    print(result)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
