import sys
from itertools import combinations_with_replacement
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc(ar):
    ret = 0
    for a, b, c, d in abcd:
        if ar[b] - ar[a] == c:
            ret += d
    return ret

if __name__ == "__main__":
    n, m, q = m_snput()
    a_l = [x for x in range(1, m+1)]
    abcd = [None] * q

    for i in range(q):
        a, b, c, d = m_snput()
        a -= 1
        b -= 1
        abcd[i] = (a, b, c, d)
    ans = 0

    for ch in combinations_with_replacement(a_l, n):
        ans = max(calc(ch), ans)
    print(ans)
    """
    m個の数字があってn個の数列に並べる
    m C nか？
    ただし重複があってもいい
    m ** nの方が正しい
    今回、n<=10、m<=10なので10 ** 10、、、だめでは...

    下はややこしい,というか最大がmなだけでm個のボール全部並べるわけではない
    長さn、最大がm
    =>m個の⚪︎とn-1本の|がある
    image => ⚪︎⚪︎|⚪︎⚪︎⚪︎⚪︎|⚪︎⚪︎
    最初からn-1本のバーがある
    今回は等しい数が数列の中にあって良いつまりバーに接するボールなくてOK
    (n-1)+m C (n-1)
    (考え方としては(n-1)+m個の椅子があってそこからバーを置くn-1個を選ぶイメージ)
    (別の考え方としてはn-1本のバーが既においてありそこにm個をどこにおいてもおかなくても良い
    と考える.

    どのバーの間にも最低一つボールがあるとするときは
    面倒なので最初からボールを配っておく(m-n) C n通りの数列がある
    *上記の類似問題abc185-c

    Ab - Aa = c => dの総和
    m以下
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
