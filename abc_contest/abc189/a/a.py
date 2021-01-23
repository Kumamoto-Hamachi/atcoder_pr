from pprint import pprint as pp
import sys
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8")
# read
# snput = sys.stdin.buffer.readline
# m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = sreadline().rstrip()
    n = set(n)
    if len(n) == 1:
        print("Won")
    else:
        print("Lost")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
