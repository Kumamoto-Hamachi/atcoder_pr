import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def sreadline(): return readline().decode("utf-8").rstrip()

def count(n):
    if n <= 125:
        return 4
    elif n <= 211:
        return 6
    else:
        return 8


if __name__ == "__main__":
    n = int(readline())
    print(count(n))
