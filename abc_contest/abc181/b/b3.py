import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())



if __name__ == "__main__":
    n = int(snput())
    ans = 0
    for i in range(n):
        a, b = m_snput()
        ans += (a + b) * (b - a  + 1) // 2
    print(ans)

