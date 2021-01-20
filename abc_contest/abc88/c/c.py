import sys
# readlines = sys.stdin.buffer.readlines
# map_readlines = lambda: map(int, readlines())
# readline = sys.stdin.buffer.readline
# map_readline = lambda: map(int, readline().split())
# sreadline = lambda: readline().decode("utf-8")
# read
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

def calc_all_b_by_a1(a1, c_l):
    b1 = c_l[0][0] - a1
    b2 = c_l[0][1] - a1
    b3 = c_l[0][2] - a1
    return b1, b2, b3

def is_same(b_l, num):
    num -= 1
    a_set = set()
    for i in range(3):
        tmp_a = c_l[num][i] - b_l[i]
        a_set.add(tmp_a)
    return len(a_set) == 1

def solve(a_opt):
    for i in range(a_opt+1):
        a1 = i
        b1, b2, b3 = calc_all_b_by_a1(a1, c_l)
        b_l = [b1, b2, b3]
        flag1 = is_same(b_l, 2)
        flag2 = is_same(b_l, 3)
        if flag1 and flag2:
            print("Yes")
            sys.exit()
    print("No")

# 流石に汚い
if __name__ == "__main__":
    c_l = [None] * 3
    for i in range(3):
        c_l[i] = list(m_snput())
    a_opt = c_l[0][0]
    solve(a_opt)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
