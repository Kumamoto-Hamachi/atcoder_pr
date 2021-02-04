import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    H, N = map_readline()
    attack_sum = sum(map_readline())
    if H <= attack_sum:
        print("Yes")
    else:
        print("No")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

