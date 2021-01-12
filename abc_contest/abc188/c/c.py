import sys
from copy import copy
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def tounament(a_l, limit):
    new_l = limit // 2
    tmp_l = [None] * new_l
    for a, b in enumerate(range(0, limit, 2)):
        tmp_l[a] = max(a_l[b] ,a_l[b+1])
    a_l = copy(tmp_l)
    if len(a_l) <= 2:
        return a_l
    limit = len(a_l)
    return tounament(a_l, limit)


if __name__ == "__main__":
    n = int(snput())
    limit = 2 ** n
    a_l = list(m_snput())
    if n == 1:
        ans = min(a_l)
        print(a_l.index(ans)+1)
        sys.exit()
    ans_l = tounament(a_l, limit)
    next_winner = min(ans_l)
    print(a_l.index(next_winner)+1)


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
