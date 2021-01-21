import sys
readline = sys.stdin.buffer.readline
sreadline = lambda: readline().decode("utf-8")
ACGT = "ACGT"

if __name__ == "__main__":
    S = sreadline()
    ans = 0
    cnt = 0
    for s in S:
        if s in ACGT:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(cnt, ans)
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
