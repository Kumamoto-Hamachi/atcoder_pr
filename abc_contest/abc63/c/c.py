from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8")
# read
# snput = sys.stdin.buffer.readline
# m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    N = int(readline())
    min_not_ten_muliti = 101
    score = 0
    for _ in range(N):
        tmp_score = int(readline())
        min_not_ten_muliti = min(min_not_ten_muliti, 101 if tmp_score % 10 == 0 else tmp_score)
        score += tmp_score
    if score % 10 != 0:
        score = score
    elif score % 10 == 0 and min_not_ten_muliti != 101:
        score -= min_not_ten_muliti
    else:
        score = 0
    print(score)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
