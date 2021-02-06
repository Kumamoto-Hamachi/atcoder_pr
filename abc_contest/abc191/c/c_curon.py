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
# Queue is very slow

def is_corner(i, j):
    count_w = 0
    if field[i][j] == ".":
        count_w += 1
    if field[i+1][j] == ".":
        count_w += 1
    if field[i][j+1] == ".":
        count_w += 1
    if field[i+1][j+1] == ".":
        count_w += 1
    if count_w == 1 or count_w == 3:
        return 1
    return 0


if __name__ == '__main__':
    h, w = list(map(int, input().split()))
    field = []
    for _ in range(h):
        field.append(input())
    #print('field') # debug
    #print(field) # debug

    count = 0
    for i in range(h-1):
        for j in range(w-1):
            if is_corner(i, j):
                count += 1
    #print('count') # debug
    print(count)


    #print('\33[32m' + 'end' + '\033[0m') # debug

