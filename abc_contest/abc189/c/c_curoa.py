#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect


def get_min(data):
    pos = -1
    m = math.inf
    for i, v in enumerate(data):
        if v < m:
            m = v
            pos = i
    return m, pos



def solve(data):
    #print('data') # debug
    #print(data) # debug
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    h, pos = get_min(data)
    #print('pos', pos) # debug
    ans_a = len(data) * h
    ans_l = solve(data[:pos])
    ans_r = solve(data[pos+1:])
    return max([ans_a, ans_l, ans_r])



if __name__ == '__main__':
    _ = int(input())
    data = list(map(int, input().split()))

    ans = solve(data)
    #print('ans') # debug
    print(ans) # debug


    #print('\33[32m' + 'end' + '\033[0m') # debug
