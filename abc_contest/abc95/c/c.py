import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

# 嘘解法？
if __name__ == "__main__":
    A, B, C, X, Y = map_readline()
    # ABなし
    ans1 = A * X + B * Y
    # Aを全部ABで
    ans2 = C * 2 * X
    rest = Y - X
    if rest > 0:
        ans2 += rest * B
    # Bを全部ABで
    ans3 = C * 2 * Y
    rest = X - Y
    if rest > 0:
        ans3 += rest * A
    ans = min(ans1, ans2, ans3)
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
