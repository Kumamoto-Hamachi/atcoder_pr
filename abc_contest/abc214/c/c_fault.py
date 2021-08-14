from pprint import pprint as pp
from collections import defaultdict
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
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    for i in range(N*2):
        T[(i+1)%N] = min(T[(i+1)%N], T[i%N] + S[i%N])

    for ans in T:
      print(ans)
