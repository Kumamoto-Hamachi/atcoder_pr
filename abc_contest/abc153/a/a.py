import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    H, A = map_readline()
    cnt = 0
    while H > 0:
        H -= A
        cnt += 1
    print(cnt)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
