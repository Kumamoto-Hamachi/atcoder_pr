import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    r1, c1 = m_snput()
    r2, c2 = m_snput()
    r = r2 - r1
    c = c2 - c1
    if (r, c) == (0, 0):
        print(0)
    elif r == c or r == -c:
        print(1)
    elif abs(r) + abs(c) <= 3:
        print(1)
        # (r, c) == (1, 1) or (0, 0) or これ(num+2, num) or (num, num+2)
        #A, B
    elif (r ^ c ^ 1) & 1:
        print(2)
        #C, C
    elif abs(r) + abs(c) <= 6:
        print(2)
        # A, C or B, C
    elif abs(r + c) <= 3 or abs(r - c) <= 3:
        print(2)
    else:
        print(3)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    |r1 - r2| + |c1 - c2| <= 3
    r + c <= 3
    """

    hoge = 0
    fuga = 2
    if (hoge ^ fuga ^ 1) & 1:
        print("unko")
    # 排他的論理和
    print((hoge ^ fuga ^ 1) & 1)
    print(bin(10))
    print(bin(2))
    print(bin(10 ^ 2))
    print(bin(hoge ^ fuga ^ 1))
