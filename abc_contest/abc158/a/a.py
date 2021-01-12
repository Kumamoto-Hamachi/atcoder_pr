import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    monopoly_pattern = ["AAA", "BBB"]
    stations = snput()
    if stations not in monopoly_pattern:
        print("Yes")
    else:
        print("No")

    """ 計算量が3 + 3になる、上だと2だけで済む(と思う)
    stations = snput()
    if "A" in stations and "B" in stations:
        print("Yes")
    else:
        print("No")
    """

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
