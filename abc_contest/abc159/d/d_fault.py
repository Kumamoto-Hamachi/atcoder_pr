import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def count(tmp_l, tmp_s):
    count = 0
    for b in tmp_s:
        tmp_count = tmp_l.count(b)
        count += calc(tmp_count)
        tmp_l = tmp_l[tmp_count:]
    return int(count)

def calc(num):
    if num < 2:
        return 0
    return (num * (num - 1) / 2)

if __name__ == "__main__":
    n = int(snput())
    hoge_d = {}
    hoge_l = [None] * n
    b_l = list(m_snput())
    for i in range(n):
        tmp_l = b_l[:]
        hoge = tmp_l.pop(i)
        if hoge not in hoge_d:
            tmp_l.sort()
            tmp_s = set(tmp_l)
            ans = count(tmp_l, tmp_s)
            hoge_d[hoge] = ans
        hoge_l[i] = hoge_d[hoge]
    for i in hoge_l:
        print(i)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
