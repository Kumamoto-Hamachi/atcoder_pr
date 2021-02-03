import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    N = int(readline())
    str_dict = defaultdict()
    for _ in range(N):
        s = sreadline()
        if s[0] != "!":
            if str_dict.get(s) == 1:
                print(s)
                sys.exit()
            str_dict[s] = 0
        else:
            if str_dict.get(s[1:]) == 0:
                print(s[1:])
                sys.exit()
            str_dict[s[1:]] = 1
    print("satisfiable")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
