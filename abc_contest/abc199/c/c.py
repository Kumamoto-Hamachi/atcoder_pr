from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


if __name__ == "__main__":
    N = int(readline())
    S = sreadline()
    s_l = [None] * (2 * N)
    n_l = [None] * (2 * N)
    for i, s in enumerate(S): #4 * 10
        s_l[i] = s
        n_l[i] = (i + N) % (2 * N)
    # print("n_l", n_l)  # debug
    Q = int(readline())
    flag = 0
    for q in range(Q): # 3 * 10
        query = list(map_readline())
        bef, aft = query[1], query[2]
        bef -= 1
        aft -= 1
        if query[0] == 1 and flag % 2 == 0:
            s_l[aft], s_l[bef] = s_l[bef], s_l[aft]
        elif query[0] == 2:
            flag += 1
        else:
            bef, aft = n_l[bef], n_l[aft]
            s_l[aft], s_l[bef] = s_l[bef], s_l[aft]
    # print("s_l", s_l)  # debug
    if flag % 2 != 0: # 4 * 10
        s_l =  s_l[N:] + s_l[:N]
    ANS = "".join(s_l)
    print(ANS)


    #"""
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
