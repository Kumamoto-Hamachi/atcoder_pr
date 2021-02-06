import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    origin = sreadline()
    bottom_flag = False
    top = ""
    bottom = ""
    Q = int(readline())
    for _ in range(Q):
        query = sreadline().split()
        if query[0] == "1":
            bottom_flag = True if not bottom_flag else False
        else:
            if bottom_flag ^ (query[1] == "2"):
                bottom += query[2]
            else:
                top += query[2]
    S = top[::-1] + origin + bottom
    if bottom_flag:
        S = S[::-1]
    print(S)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

