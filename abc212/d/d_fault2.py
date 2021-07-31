import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    Q = int(readline())
    knap = set()
    added = 0
    for _ in range(Q):
        query = list(map_readline())
        if query[0] == 1:
            knap.add(query[1] - added)
        elif query[0] == 2:
            added += query[1]
        else:
            min_ball = min(knap)
            knap.remove(min_ball)
            print(min_ball + added)
