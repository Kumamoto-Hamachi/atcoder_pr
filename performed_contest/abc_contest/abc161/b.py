import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, m = m_snput()
    a_list = list(m_snput())
    limit_rate = 1 / (4 * m)
    a_sum = sum(a_list)
    a_len = len(a_list)
    # もう少しここらへん美しく書き直しして
    if a_len < m:
        print("No")
        sys.exit()
    a_list.sort(reverse=True)
    for i in range(m):
        if a_list[i] / a_sum < limit_rate:
            print("No")
            sys.exit()
    print("Yes")
