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
    N, X = map_readline()
    X *= 100
    for i in range(N):
        V, P = map_readline()
        X -= V * P
        if X < 0:
            print(i+1)
            sys.exit()
    print(-1)


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
