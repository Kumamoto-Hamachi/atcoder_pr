import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

# the simplest way of three
if __name__ == "__main__":
    while True:
        n, x = map_readline()
        cnt = 0
        if n == 0 and x == 0:
            break
        for a in range(1, n+1):
            for b in range(a+1, n+1):
                for c in range(b+1, n+1):
                    cnt += 1 if a + b + c == x else 0
        print(cnt)
