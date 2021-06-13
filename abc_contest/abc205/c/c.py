from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
sreadlines = lambda: [s.decode("utf-8").rstrip() for s in readlines()] # return strs per line list

if __name__ == "__main__":
    A, B, C = map_readline()
    pow_ac = A
    pow_bc = B
    if A == B:
        print("=")
        sys.exit()
    if abs(A) == abs(B) and C % 2 == 0:
        print("=")
        sys.exit()

    if A >= 0 and B >= 0:
        if A > B:
            print(">")
        else:
            print("<")
    elif A * B >= 0: #両方マイナス
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            else:
                print("<")
        else:
            if abs(A) > abs(B):
                print("<")
            else:
                print(">")
    else: #片方マイナス
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            else:
                print("<")
        else:
            if A > B:
                print(">")
            else:
                print("<")

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    low_english_literature = " ".join(sreadlines())
    """
