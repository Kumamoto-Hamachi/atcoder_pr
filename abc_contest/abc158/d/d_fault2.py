import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    # これですらTLEになる
    S = snput()
    Q = int(snput())
    cnt = 0
    for _ in range(Q):
        q_l = snput().split()
        if q_l[0] == "1":
            cnt = 0 if cnt else 1
        else:
            head_or_ass = int(q_l[1])
            additional_s = q_l[2]
            if (cnt + head_or_ass) % 2 == 0:
                S += additional_s
            else:
                S = additional_s + S
    if cnt == 0:
        print(S)
    else:
        print(S[::-1])

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
