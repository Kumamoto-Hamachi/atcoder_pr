import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())


def is_contradiction(requirement_l, s, c, digit):
    if (requirement_l[s-1] is not None and requirement_l[s-1] != c) or\
    (s == 1 and c == 0 and digit > 1):
        return True
    return False


# 関数名ビミョー？
def be_must_topmost_1(digit, requirement_l):
    if digit > 1 and requirement_l[0] is None:
        return True
    return False

# ムズカシく考えすぎ/書きすぎ
if __name__ == "__main__":
    digit, codition_cnt = m_snput()
    requirement_l = [None] * digit
    for _ in range(codition_cnt):
        s, c = m_snput()
        if is_contradiction(requirement_l, s, c, digit):
            print(-1)
            sys.exit()
        requirement_l[s-1] = c
    if be_must_topmost_1(digit, requirement_l):
        requirement_l[0] = 1
    digit_l = [i if i is not None else 0 for i in requirement_l]
    print("".join(map(str, digit_l)))

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
