import sys
import itertools
from copy import deepcopy

snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    h, w, k = m_snput()
    h_l = [0] * 2 ** h
    w_l = [0] * 2 ** w
    square_l = [None] * h
    for i in range(h):
        s = list(snput())
        s = [True if i == "#" else False for i in s]
        square_l[i] = s

    for i in range(2 ** h):
        s = bin(i)
        h_l[i] = s[2:]
    for i in range(2 ** w):
        s = bin(i)
        w_l[i] = s[2:]
    hw = list(itertools.product(h_l, w_l))
    count = 0
    for a, b in hw:
        tmp_l = deepcopy(square_l)
        for i, s in enumerate(a):
            if int(s):
                tmp_l[i] = [False] * w
        for i, s in enumerate(b):
            if int(s):
                for j in range(h):
                    tmp_l[j][i] = False
        sum_t = sum(map(sum, tmp_l))
        if sum_t == k:
            print("a, b", a, b)  # debug
            count += 1
    print(count)






    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
