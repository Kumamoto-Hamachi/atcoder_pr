import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sys.setrecursionlimit(10 ** 7)
MAX_A = 10 ** 5 + 1


def get_min(a_l):
    min_hight = MAX_A
    order = 0
    for i, a in enumerate(a_l):
        if a < min_hight:
            min_hight = a
            order = i
    return min_hight, order


def split_search(a_l):
    if len(a_l) == 0:
        return 0
    if len(a_l) == 1:
        return a_l[0]
    h, order = get_min(a_l)
    lr = len(a_l) * h
    l = split_search(a_l[:order])
    r = split_search(a_l[order+1:])
    return max(lr, l, r)


if __name__ == "__main__":
    N = int(readline())
    a_l = list(map_readline())
    ans = split_search(a_l)
    print(ans)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
