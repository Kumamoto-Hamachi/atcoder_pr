import sys, math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    l = int(snput())
    l -= 1 # 切り目候補
    """
    l - 1 C 11
    """
    ans = 1
    for i in range(11):
        ans *= (l - i)
        ans //= (i + 1)
    print(ans)

