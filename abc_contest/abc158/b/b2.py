import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, blue_lot, red_lot = m_snput()
    blue = n // (blue_lot + red_lot) * blue_lot
    rest = n % (blue_lot + red_lot)
    blue += min(blue_lot, rest)
    print(blue)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
