import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())
BINGO = 3

def judge_num(n, bing_l):
    for i, b_l in enumerate(bing_l):
        if n in b_l:
            b = b_l.index(n)
            return (i, b)
    return (-1, -1)

def is_bingo1(bing_l):
    for b_l in bing_l:
        for i, b in enumerate(b_l):
            if b:
                break
            if i == 2:
                return True
    return False


def is_bingo2(bing_l):
    for a in range(BINGO):
        for b in range(BINGO):
            if bing_l[b][a]:
                break
            if b == 2:
                return True
    return False


def is_bingo3(bing_l):
    for i in range(BINGO):
        if bing_l[i][i]:
            return False
    return True

def is_bingo4(bing_l):
    for i in range(BINGO):
        if bing_l[i][BINGO - i - 1]:
            return False
    return True



# 糞コードすぎる -> b2.pyにて書き直し済
if __name__ == "__main__":
    bing_l = [None] * BINGO
    for i in range(BINGO):
        bing_l[i] = list(m_snput())
    N = int(snput())
    i, b = judge_num(0, bing_l)
    bing_l[i][b] = 1
    for _  in range(N):
        n = int(snput())
        i, b = judge_num(n, bing_l)
        bing_l[i][b] = None
    if is_bingo1(bing_l) or is_bingo2(bing_l) or is_bingo3(bing_l) or is_bingo4(bing_l):
        print("Yes")
    else:
        print("No")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
