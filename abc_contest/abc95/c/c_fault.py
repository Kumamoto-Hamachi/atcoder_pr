import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

"""
1001 1000 999 105 1
CのみでAの分
CのみでBの分
AB
"""

if __name__ == "__main__":
    A, B, C, X, Y = map_readline()
    tmp = A * X + B * Y
    if A + B <= 2 * C:
        ans = tmp
    # もう少しだが
    elif A > B and C * 2 * X < tmp:
        ans = C * 2 * X
        rest = Y - X
        if rest > 0:
            ans += rest * B
    else:
        ans = C * 2 * Y
        rest = X - Y
        if rest > 0:
            ans += rest * A
    print(ans)

    """
    S = min(X, Y)
    T = max(X, Y) - S
    (A + B) * S ? (2 * C) * S
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
