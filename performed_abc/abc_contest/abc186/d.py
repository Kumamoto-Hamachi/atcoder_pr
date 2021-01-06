import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    n_list = list(m_snput())
    n_list.sort()
    upper = n_list[:]
    # range(start, stop, step)
    for i in range(n - 2, -1, -1):
        upper[i] += upper[i+1]
    ans = 0
    for i in range(n-1):
        ans += upper[i+1] - n_list[i] * (n - i - 1)
    print(ans)
