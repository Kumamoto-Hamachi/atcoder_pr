from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def exchange(num_dict, N):
    print("num_dict", num_dict)  # debug

if __name__ == "__main__":
    N = int(readline())
    S = sreadline()
    s_dict = {}
    num_dict = {}
    for i, s in enumerate(S):
        s_dict[i+1] = s
        num_dict[i+1] = i+1
    #"""
    Q = int(readline())
    for q in range(Q):
        query = list(map_readline())
        if query[0] == 1:
            bef, aft = query[1], query[2]
            num_dict[aft], num_dict[bef] = num_dict[bef], num_dict[aft]
        else:
            exchange(num_dict, N)
    # print("num_dict", num_dict)  # debug
    ANS = ""
    for k, v in num_dict.items():
        ANS += s_dict[v]
    # print(ANS)

    #"""
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
