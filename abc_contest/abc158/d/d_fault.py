import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    # TLE
    S = snput()
    Q = int(snput())
    for _ in range(Q):
        query_l = snput().split()
        if query_l[0] == "1":
            S = S[::-1]
        else:
            additional_s = query_l[2]
            if query_l[1] == "1":
                S = additional_s + S
            else:
                S += additional_s
    print(S)


    """
    1 s[::-1]
    2 fi ci
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
