import sys
import math
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
A = 4
B = 7


if __name__ == "__main__":
    n = int(readline())
    max_item = n // A
    for i in range(max_item+1):
        a_item = max_item - i
        cost = (n - a_item * A) / B
        if int(cost) == math.ceil(cost):
            print("Yes")
            sys.exit()
    print("No")
