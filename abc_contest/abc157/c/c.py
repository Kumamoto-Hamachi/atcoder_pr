import sys
snput = lambda: sys.stdin.readline()
# snput = lambda: sys.stdin.buffer.readline() # TODO
m_snput = lambda: map(int, snput().split())

# 意地の悪い問題
if __name__ == "__main__":
    n, m = m_snput()
    if n == 1 and m == 0:
        print(0)
        sys.exit()
    num_l = [None] * n
    for _ in range(m):
        s, c = m_snput()
        if num_l[s-1] is None or num_l[s-1] == c:
            num_l[s-1] = c
        else:
            print(-1)
            sys.exit()
    # print("num_l", num_l)  # debug
    if num_l[0] is None:
        num_l[0] = 1
    num_l = [i if i is not None else 0 for i in num_l]
    # print("num_l", num_l)  # debug
    if num_l[0] == 0 and n != 1:
        print(-1)
        sys.exit()
    print("".join(map(str, num_l)))

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
