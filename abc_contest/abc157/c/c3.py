import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    digit, condition_num = m_snput()
    condition_list = [None] * digit
    for _ in range(condition_num):
        s, c = m_snput()
        if condition_list[s-1] is not None and condition_list[s-1] != c:
            print(-1)
            sys.exit()
        condition_list[s-1] = c
    if condition_list[0] == 0 and digit > 1:
        print(-1)
        sys.exit()
    num = ""
    for c in condition_list:
        num += str(c) if c is not None else "0"
    if num[0] == "0" and digit > 1:
        num = "1" + num[1:]
    print(num)

    """
    日本語化
    桁数と条件の個数が与えられます
    その後に「何桁目の数字は*ですよ。」という条件が着ます。
    終わったあとに条件をを満たす数字のうち最小のものを答えてください。
    ただし、与えられた条件が矛盾を発生させるものもあるのでそのときはそんな数字はないと答えてください。
    """
