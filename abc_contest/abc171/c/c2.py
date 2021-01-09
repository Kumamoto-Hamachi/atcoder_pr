import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    rows = 1
    dog_name = ""
    while True:
        n -= 26 ** rows
        if n <= 0:
            n += 26 ** rows
            break
        rows += 1
    # aが0、zが25の26進数
    n -= 1
    # print("n", n)  # debug
    for i, r in enumerate(range(rows-1, -1, -1)):
        # print("r", r)  # debug
        digit = 26 ** r
        c = n // digit
        dog_name += chr(97+c)
        n -= c * digit
    print(dog_name)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
