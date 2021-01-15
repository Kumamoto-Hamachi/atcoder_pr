import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())
BINGO = 3

def record_bingo(num, bingo_l, records):
    for r in range(BINGO):
        for c in range(BINGO):
            if num == bingo_l[r][c]:
               records[r][c] = True
               return records
    return records

# 行列が大きくなった場合に備えて(かえってややこしいかな...)
def is_bingo_by_horizontal_row(records):
    for row in records:
        for i in range(BINGO):
            if not row[i]:
                break
            if i == BINGO - 1:
                return True
    return False

def is_bingo_by_vertical_row(records):
    for c in range(BINGO):
        for r in range(BINGO):
            if not records[r][c]:
                break
            if r == BINGO - 1:
                return True
    return False


def is_bingo_by_left_shoulder(records):
    for i in range(BINGO):
        if not records[i][i]:
            break
        if i == BINGO - 1:
            return True
    return False


def is_bingo_by_right_shoulder(records):
    for i in range(BINGO):
        if not records[i][BINGO-i-1]:
            break
        if i == BINGO - 1:
            return True
    return False

if __name__ == "__main__":
    bingo_l = [None] * BINGO
    for i in range(BINGO):
        bingo_l[i] = list(m_snput())
    # records = [[False] * BINGO] * BINGO この書き方は副作用が出る！注意！
    records = [[False, False, False], [False, False, False], [False, False, False]]
    N = int(snput())
    for _ in range(N):
        num = int(snput())
        records = record_bingo(num, bingo_l, records)
    if is_bingo_by_horizontal_row(records) or\
    is_bingo_by_vertical_row(records) or\
    is_bingo_by_left_shoulder(records) or\
    is_bingo_by_right_shoulder(records):
        print("Yes")
    else:
        print("No")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
