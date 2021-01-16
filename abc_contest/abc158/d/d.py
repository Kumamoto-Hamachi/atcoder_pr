import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    origin_s = snput()
    q = int(snput())
    cnt = 0
    head_s = ""
    bottom_s = ""
    for _ in range(q):
        query_l = snput().split()
        if query_l[0] == "1":
            cnt = 1 if cnt == 0 else 0
        else:
            head_or_bottom = int(query_l[1]) # 1 or 2
            additional_s = query_l[2]
            if (cnt + head_or_bottom) % 2 == 1:
                head_s += additional_s
            else:
                bottom_s += additional_s
    head_s = head_s[::-1]
    S = head_s + origin_s + bottom_s
    if cnt == 0:
        print(S)
    else:
        print(S[::-1])

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
