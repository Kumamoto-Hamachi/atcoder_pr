import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    N = int(readline())
    for a in map_readline():
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print("DENIED")
                sys.exit()
    print("APPROVED")


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
