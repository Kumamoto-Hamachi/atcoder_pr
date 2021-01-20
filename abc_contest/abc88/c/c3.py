import sys
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8")
NUM = 3

def calc_b_by_a1(a1, c_l):
    b1 = c_l[0][0] - a1
    b2 = c_l[0][1] - a1
    b3 = c_l[0][2] - a1
    return b1, b2, b3


def check_specified_a_is_same(b_l, c_l):
    for i in range(1, NUM):
        a_set = set()
        order = i
        for j in range(NUM):
            a = c_l[order][j] - b_l[j]
            a_set.add(a)
        if len(a_set) != 1:
            return False
    return True


if __name__ == "__main__":
    c_l = [None] * NUM
    for i in range(NUM):
        c_l[i] = list(map_readline())
    a1 = 0
    b_l = calc_b_by_a1(a1, c_l)
    if check_specified_a_is_same(b_l, c_l):
        print("Yes")
    else:
        print("No")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
