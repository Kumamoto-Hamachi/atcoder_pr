import sys
# readlines = sys.stdin.buffer.readlines
# map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
# map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8")
# read
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    S = sreadline()
    ACGT = "ACGT"
    cnt = 0
    max_cnt = 0
    for i, s in enumerate(S):
        if s in ACGT:
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 0
    max_cnt = max(cnt, max_cnt)
    print(max_cnt)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
