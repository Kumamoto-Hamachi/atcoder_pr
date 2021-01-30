import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    N = int(readline())
    a_map = map_readline()
    a_even_map = (a for a in a_map if a % 2 == 0)
    for a in a_even_map:
        if a % 3 == 0:
            continue
        elif a % 5 == 0:
            continue
        else:
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
