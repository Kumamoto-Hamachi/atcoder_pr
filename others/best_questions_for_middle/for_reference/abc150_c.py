from itertools import permutations
import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]


if __name__ == "__main__":
    n = int(readline())
    a_list = list(map_readline())
    b_list = list(map_readline())
    num_list = [i for i in range(1, n+1)]
    num_list_set = permutations(num_list)
    for i, nl in enumerate(num_list_set):
        nl = list(nl)
        if nl == a_list:
            aidx = i
        if nl == b_list: # はじめelifで考えたがコーナーケースを考えよう!
            bidx = i
    ans = abs(aidx - bidx)
    print(ans)
