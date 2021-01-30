import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    s, t = sreadline().split(" ")
    a, b = map_readline()
    ball_color = sreadline()
    if s == ball_color:
        a -= 1
    else:
        b -= 1
    print(a, b)
    # print([f"{a-1} {b}",f"{a} {b-1}"][t==input()])
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
