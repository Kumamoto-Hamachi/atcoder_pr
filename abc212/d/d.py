import sys
from heapq import heappush, heappop
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    Q = int(readline())
    added = 0
    hp = []
    for _ in range(Q):
        query = list(map_readline())
        if query[0] == 1:
            heappush(hp, query[1] - added)
        elif query[0] == 2:
            added += query[1]
        else:
            min_ball = heappop(hp)
            print(min_ball + added)
