import sys
readline = sys.stdin.buffer.readline


if __name__ == "__main__":
    n = int(readline())
    cnt = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            cnt += 1
    print(cnt)
