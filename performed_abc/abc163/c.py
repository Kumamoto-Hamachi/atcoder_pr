import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    a_l = list(m_snput())
    a_c = [0] * n
    for a in a_l:
        a_c[a-1] += 1
    for c in a_c:
        print(c)

    """ なぜこれだとTLEになるのか => n回count(n個見る動作) = n ** 2今回だとn <= 10 ** 5となる
    この計算量はきついよね
    for i in range(1, n+1):
        print(a_l.count(i))
    """

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
