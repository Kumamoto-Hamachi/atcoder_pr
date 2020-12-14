import sys, math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    l = int(snput())
    l -= 12 # 先にボールを配り終わっておく
    ball = l
    # print("ball", ball)  # debug
    l += 11
    ans = 1
    for i in reversed(range(1, l + 1)):
        ans *= i
    for i in range(1, 11+1):
        ans //= i
    for i in range(1, ball+1):
        ans //= i
    # print("ans", ans)  # debug
    print(ans)
