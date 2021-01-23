import sys
import numpy as np
readlines = sys.stdin.buffer.readlines
# map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
# sreadline = lambda: readline().decode("utf-8")
# read
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())
BINGO = 3


def mark_record(b_l, bingo, records):
    for b in b_l:
        row, column = show_index(b, bingo)
        if row != -1 and column != -1:
            records[row][column] = 1
    return records


def show_index(b, bingo):
    for row in range(BINGO):
        if b in bingo[row]:
            column = bingo[row].index(b)
            return row, column
    return -1, -1


# TODO
# 直線上が全て1
def check_straight(records):
    x_l = [0] * BINGO
    y_l = [0] * BINGO
    # print("records", records)  # debug
    for i in range(BINGO):
        for j in range(BINGO):
            if records[i][j]:
                x_l[j] += 1
                y_l[i] += 1
    # print("x_l, y_l", x_l, y_l)  # debug
    # ダメ (0, 1)(1, 0)(2, 2)を弾けない
    if BINGO in x_l or BINGO in y_l or is_left(x_l, y_l) or is_right(x_l, y_l):
        return True
    else:
        return False


def is_left(x_l, y_l):
    for i in range(BINGO):
        if not x_l[i] or not y_l[i]:
            return False
    return True


def is_right(x_l, y_l):
    for i in range(BINGO):
        if not x_l[i] or not y_l[BINGO-i]:
            return False
    return True


if __name__ == "__main__":
    records = [[0 for _ in range(BINGO)] for _ in range(BINGO)]
    bingo = [list(map_readline()) for _ in range(BINGO)]
    n, *b_l = map(int, readlines())
    records = mark_record(b_l, bingo, records)
    print("Yes" if check_straight(records) else "No")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
