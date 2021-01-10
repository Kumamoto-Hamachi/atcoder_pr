import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    a_l = list(m_snput())
    b_l = list(m_snput())
    a_len = len(a_l)
    ans = 0
    for i in range(a_len):
        ans += (a_l[i] * b_l[i])
    if ans == 0:
        print("Yes")
    else:
        print("No")
