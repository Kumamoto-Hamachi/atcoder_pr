import sys
import collections
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc(num):
    if num < 2:
        return 0
    return int(num * (num-1) / 2)

def count(num, b_d):
    ans = 0
    for b in b_d:
        if num == b:
            ans += calc(b_d[b]-1)
        else:
            ans += calc(b_d[b])
    return ans


if __name__ == "__main__":
    n = int(snput())
    b_l = list(m_snput())
    b_d = {}
    hoge_d = {}
    c = collections.Counter(b_l)
    for b in c.most_common():
        b_d[b[0]] = b[1]
    for i in range(n):
        num = b_l[i]
        if num not in hoge_d:
            hoge_d[num] = count(num, b_d)
        print(hoge_d[num])

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
