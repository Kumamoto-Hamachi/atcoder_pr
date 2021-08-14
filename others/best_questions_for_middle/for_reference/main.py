import sys
readline = sys.stdin.buffer.readline


def count_divisor(num):
    limit = int(num ** 0.5) + 1
    cnt = 0
    for i in range(1, limit):
        if num % i == 0:
            cnt += 1
            quotient = num // i
            if quotient != i:
                cnt += 1
    return cnt


if __name__ == "__main__":
    n = int(readline())
    ans = 0
    for i in range(1, n+1, 2):
        if count_divisor(i) == 8:
            ans += 1
    print(ans)
