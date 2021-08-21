from pprint import pprint as pp
from collections import defaultdict
import sys
import itertools
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]


if __name__ == "__main__":
    s, k = sreadline().split(" ")
    k = int(k)
    #s_list = list(s)
    s_len = len(s)
    s_idx = list(range(s_len))
    idx_patterns = list(itertools.permutations(s_idx))

    all_s = []
    for idx_pattern in idx_patterns:
        tmp = ""
        for idx in idx_pattern:
            tmp += s[idx]
        all_s.append(tmp)
    all_s = list(set(all_s))
    all_s = sorted(all_s)
    #print("all_s", all_s)  # debug
    print(all_s[k-1])

