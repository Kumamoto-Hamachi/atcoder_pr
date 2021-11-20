from pprint import pprint as pp
from collections import defaultdict
from itertools import permutations
import sys
import math
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def list_readline(): return list(map_readline())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]
MAX = 300


if __name__ == "__main__":
    n, k = list_readline()
    student_dict = {}
    ranking = [None] * n
    for i in range(n):
        score = sum(list_readline())
        ranking[i] = score
    sorted_ranking = sorted(ranking, reverse=True)
    for s in ranking:
        if sorted_ranking[k-1] <= s + MAX:
            print("Yes")
        else:
            print("No")
