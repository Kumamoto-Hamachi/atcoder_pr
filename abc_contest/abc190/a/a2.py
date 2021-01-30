import sys
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    a, b, c = map_readline()
    if a > b - c:
        print("Takahashi")
    else:
        print("Aoki")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
