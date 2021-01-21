import sys
readline = sys.stdin.buffer.readline
sreadline = lambda: readline().decode("utf-8")
ACGT = "ACGT"

if __name__ == "__main__":
    S = sreadline()
    N = len(S)
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if all(ACGT.count(c) == 1 for c in S[i:j+1]):
                # print("S[i:j+1]", S[i:j+1])  # debug
                ans = max(ans, j - i + 1)
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
