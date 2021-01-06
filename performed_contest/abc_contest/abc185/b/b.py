import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, m, t = m_snput()
    cafe_l = [None] * m
    for i in range(m):
        cafe_l[i] = list(m_snput())
    now = 0
    btr = n
    for i in cafe_l:
        cusume_time = i[0] - now
        btr -= cusume_time
        if btr <= 0:
            print("No")
            sys.exit()
        btr += (i[1] - i[0])
        if btr > n:
            btr = n
        now = i[1]
    if btr > t - now:
        print("Yes")
    else:
        print("No")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
