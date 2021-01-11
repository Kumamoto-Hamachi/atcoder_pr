import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    ball_num, blue_lot, red_lot = m_snput()
    blue_ball = 0
    rest_ball = ball_num
    blue_red_setnum = rest_ball // (blue_lot + red_lot)
    blue_ball += blue_lot * blue_red_setnum
    rest_ball -= (blue_lot + red_lot) * blue_red_setnum
    if rest_ball >= blue_lot:
        blue_ball += blue_lot
    else:
        blue_ball += rest_ball
    print(blue_ball)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
