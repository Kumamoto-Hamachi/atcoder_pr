import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
NUM = 3


def calc_column_num_list(row0, grids):
    column_num_list = [None] * NUM
    for i in range(NUM):
        column_num_list[i] = grids[0][i] - row0
    return column_num_list


def is_contradiction_column(grids, column_num_list):
    for column in range(1, NUM):
        b = None
        for row in range(NUM):
            tmp_b = grids[column][row] - column_num_list[row]
            if b is None:
                b = tmp_b
            if b != tmp_b:
                return True
    return False


if __name__ == "__main__":
    grids = [None] * NUM
    for i in range(NUM):
        grids[i] = list(map_readline())
    # a1 = 0とする a1の範囲は実質決まっていないので全探索出来ないというのもあるが乱暴すぎないか？
    a1 = 0
    b_column_num_list = calc_column_num_list(a1, grids)
    if is_contradiction_column(grids, b_column_num_list):
        print("No")
    else:
        print("Yes")
    """
    # grids = [[None] * 3 for _ in range(3)] # 二重配列
    整数 = 0と自然数および自然数に負号をつけたもの
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
