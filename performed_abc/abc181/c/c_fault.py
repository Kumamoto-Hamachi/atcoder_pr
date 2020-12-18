import sys
from itertools import combinations
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# なぜか解けない,,,おそらく割り算のところが原因と思われる
def calc_slope(xa, ya, xb, yb):
        if xb - xa != 0:
            slope = (yb - ya) / (xb - xa)
        else:
            slope = 0.0
        if xb < xa:
            slope = abs(slope)
        return slope

if __name__ == "__main__":
    n = int(snput())
    point_list = [None] * n
    for i in range(n):
        point_list[i] = list(m_snput())
    point_c = (combinations(point_list, 3))
    for i, c in enumerate(point_c):
        y3 = c[2][1]
        y2 = c[1][1]
        y1 = c[0][1]
        x3 = c[2][0]
        x2 = c[1][0]
        x1 = c[0][0]
        slope1 = calc_slope(x1, y1, x2, y2)
        slope2 = calc_slope(x1, y1, x3, y3)
        slope3 = calc_slope(x2, y2, x3, y3)
        if slope1 == slope2 and slope2 == slope3:
            print("x1, y1, x2, y2, x3, y3", x1, y1, x2, y2, x3, y3)  # debug
            print("Yes")
            sys.exit()
    print("No")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
