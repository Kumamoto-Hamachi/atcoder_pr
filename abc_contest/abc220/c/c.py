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
R = 10 ** 100


def additional(x, a_list):
    for i, a in enumerate(a_list):
        x -= a
        #print("x", x)  # debug
        if x < 0:
            return i + 1


if __name__ == "__main__":
    n = int(readline())
    a_list = list_readline()
    a_sum = sum(a_list)
    x = int(readline())

    groups = x // a_sum
    if x % a_sum == 0:
        print(groups * n + 1)
        sys.exit()
    #print("groups", groups)  # debug
    x -= groups * a_sum
    #print("groups", groups)  # debug
    #print("x", x)  # debug
    cnt = additional(x, a_list)
    print(groups * n + cnt)
