import sys
import itertools
from copy import deepcopy
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    H, W, K = m_snput()
    h_l = [i for i in range(H+1)]
    w_l = [i for i in range(W+1)]
    hw = itertools.product(h_l, w_l)
    square_l = [None] * H
    for i in range(H):
        tmp_l = list(snput())
        square_l[i] = [False if H == "." else True for H in tmp_l]
    print("square_l", square_l)  # debug
    count = 0
    for h, w in hw:
        tmp_l = deepcopy(square_l)
        h -= 1
        w -= 1
        if h >= 0:
            tmp_l[h] = [False] * W
        if w >= 0:
            for i in range(H):
                tmp_l[i][w] = False
        blacked = sum(map(sum, tmp_l))
        print("blacked", blacked)  # debug
        print(h+1, w+1)
        if blacked == K:
            count += 1
    print(count)


    """
    . white # black
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
