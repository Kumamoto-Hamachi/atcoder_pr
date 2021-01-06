import sys
from itertools import combinations
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# 外積
def calc_cross_p(xa, ya, xb, yb, xc, yc):
    cross_p = abs((xb -xa) * (yc - ya) - (xc - xa) * (yb - ya)) / 2
    return cross_p

if __name__ == "__main__":
    n = int(snput())
    point_list = [None] * n
    for i in range(n):
        point_list[i] = list(m_snput())
    point_c = list(combinations(point_list, 3))
    for c in point_c:
        y3 = c[2][1]
        y2 = c[1][1]
        y1 = c[0][1]
        x3 = c[2][0]
        x2 = c[1][0]
        x1 = c[0][0]
        cross_p = calc_cross_p(x1, y1, x2, y2, x3, y3)
        if cross_p == 0:
            print("Yes")
            sys.exit()
    print("No")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
