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

def convert_k_to_10(k_num, k):
    digit = len(k_num)
    num = 0
    for d in range(digit):
        idx = (digit - d - 1)
        num += (k ** d) * int(k_num[idx])
    return num



if __name__ == "__main__":
    k = int(readline())
    a, b = sreadline().split(" ")
    a = convert_k_to_10(a, k)
    b = convert_k_to_10(b, k)
    print(a * b)
