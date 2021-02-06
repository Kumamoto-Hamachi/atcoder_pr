import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    H, N = map_readline()
    a_l = list(map_readline())
    a_l.sort(reverse=True)
    for a in a_l:
        H -= a
        if H <= 0:
            print("Yes")
            sys.exit()
    print("No")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
