from pprint import pprint as pp
from collections import defaultdict
import sys
import itertools
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


def count(sure, unknown):
    if len(sure) + len(unknown) == 0:
        ans = 0
    elif len(sure) > 4:
        ans = 0
    elif len(unknown) == 10:
        ans = 10000
    else:
        all_list = []
        candidates = sure + unknown
        candidate_num = len(candidates)
        true_num = candidate_num
        candidate_num = 4 if candidate_num < 4 else candidate_num
        for i in range(candidate_num-3):
            i = i % true_num
            for j in range(i+1, candidate_num-2):
                j = j % true_num
                for k in range(j+1, candidate_num-1):
                    k = k % true_num
                    for l in range(k+1, candidate_num):
                        l = l % true_num
                        cadidate_l = [candidates[i], candidates[j], candidates[k], candidates[l]]
                        all_list += add(cadidate_l)
        clear_l = check(sure, all_list)
        ans = len(clear_l)
    return ans



def add(cadidate_l):
    tmp_l = [None] * (4 ** 4)
    order = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    tmp_l[order] = [cadidate_l[i], cadidate_l[j], cadidate_l[k], cadidate_l[l]]
                    order += 1
    return tmp_l

def check(sure, all_list):
    clear_l = []
    for c_l in all_list:
        flag = True
        for s in sure:
            if s not in c_l:
                flag = False
        if flag:
            if c_l not in clear_l:
                clear_l.append(c_l)
    return clear_l



if __name__ == "__main__":
    S = sreadline()
    sure = []
    unknown = []
    for i, s in enumerate(S):
        if s == "o":
            sure.append(i)
        elif s == "?":
            unknown.append(i)
    ans = count(sure, unknown)
    print(ans)
