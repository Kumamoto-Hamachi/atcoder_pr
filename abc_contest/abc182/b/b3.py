import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    a_list = list(m_snput())
    range_num = max(a_list)
    ans = -1
    mx = 0
    for x in range(2, range_num + 1):
        # using generator expression
        s = sum(a % x == 0 for a in a_list)
        if mx <= s:
            mx = s
            ans = x
    print(ans)
