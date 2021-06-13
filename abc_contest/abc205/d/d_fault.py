from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
sreadlines = lambda: [s.decode("utf-8").rstrip() for s in readlines()] # return strs per line list

def calc_tarinai(first ,tarinai, c_l, k):
    next_index = first + tarinai
    tmp = sum(c_l[:next_index])
    if  tmp == k:
        return next_index
    else:
        tarinai = k - tmp
        first = next_index
        return calc_tarinai(first, tarinai, c_l, k)


if __name__ == "__main__":
    n, q = map_readline()
    a_l = list(map_readline())
    last_num = a_l[-1]
    rest = last_num - n
    c_l = [True] * last_num
    for a in a_l:
        c_l[a-1] = False
    for _ in range(q):
        k = int(readline())
        if k > rest:
            print(k-rest+last_num)
        else:
            tmp = sum(c_l[:k])
            if tmp == k:
                print(k)
            else:
                tarinai = k - tmp
                ans = calc_tarinai(k, tarinai, c_l, k)
                print(ans)

    """
    n 10 ** 5
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    low_english_literature = " ".join(sreadlines())
    """
