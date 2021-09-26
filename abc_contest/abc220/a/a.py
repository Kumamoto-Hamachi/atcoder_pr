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


if __name__ == "__main__":
    a, b, c = list_readline()
    hoge = (a // c) 
    if hoge * c >= a:
        if hoge * c <= b:
            print(hoge * c)
            sys.exit()
    else:
        if (hoge + 1) * c >= a:
            if (hoge + 1) * c <= b:
                hoge += 1
                print(hoge * c)
                sys.exit()
    print(-1)
