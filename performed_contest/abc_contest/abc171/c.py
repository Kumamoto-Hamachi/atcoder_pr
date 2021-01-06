import sys
from math import log, ceil, floor
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def count(num):
    pass

def calc_order_and_row(num):
    i = 0
    while True:
        i += 1
        num -= 26 ** i
        # print("num", num)  # debug
        if num <= 0:
            num += 26 ** i
            break
    return num, i

def judge_dname(num, row, dname_l):
    # print("cleaned num", num)  # debug
    for i, r in enumerate(range(row-1, -1, -1)):
        tmp = ceil(num / (26 ** r))
        num -= 26 ** r * (tmp - 1)
        # print("num", num)  # debug
        # print("tmp", tmp)  # debug
        dname_l[i] = chr(tmp+96)
    # print("dname_l", dname_l)  # debug
    return dname_l

# ゴミコード過ぎる...
if __name__ == "__main__":
    n = int(snput())
    n, row = calc_order_and_row(n)
    dname_l = [None] * row
    dname_l = judge_dname(n, row, dname_l)
    dname = "".join(dname_l)
    print(dname)
