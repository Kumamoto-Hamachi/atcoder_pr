import sys
from copy import copy
# snput = sys.stdin.buffer.readline
readline = lambda: sys.stdin.readline().rstrip()
# m_snput = lambda: map(int, snput().split())
m_snput = lambda: map(int, readline().split())

# snputだとstr読み込みに問題が出る
if __name__ == "__main__":
    S = list(readline())
    N = int(readline())
    for _ in range(N):
        r, l = m_snput()
        tmp = copy(S[r-1:l])
        S[r-1:l] = tmp[::-1]
    S = "".join(S)
    print(S)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
