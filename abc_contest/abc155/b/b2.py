import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    N = int(readline())
    a_gen = (i for i in map_readline() if i % 2 == 0)
    denied_list = [i for i in a_gen if i % 3 != 0 and i % 5 != 0]
    print("DENIED" if denied_list else "APPROVED")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
