from pprint import pprint as pp
from collections import defaultdict
import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
PREFIX = "!"

if __name__ == "__main__":
    N = int(readline())
    str_dict = dict()
    for _ in range(N):
        s = sreadline()
        if s[0] == PREFIX:
            if str_dict.get(s[1:]) == "NON_PREFIX":
                print(s[1:])
                sys.exit()
            str_dict[s[1:]] = "PREFIX"
        else:
            if str_dict.get(s) == "PREFIX":
                print(s)
                sys.exit()
            str_dict[s] = "NON_PREFIX"
    print("satisfiable")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

