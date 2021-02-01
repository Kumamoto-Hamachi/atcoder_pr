from pprint import pprint as pp
from collections import defaultdict
import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

# できるだけ標準関数を使わずに実装出来るように
if __name__ == "__main__":
    N = int(readline())
    vote_dict = {}
    for _ in range(N):
        candidate = sreadline()
        if candidate not in vote_dict:
            vote_dict[candidate] = 0
        vote_dict[candidate] += 1
    max_votes = max(vote_dict.values())
    candidates = []
    for c, v in vote_dict.items():
        if v == max_votes:
            candidates.append(c)
    candidates = sorted(candidates)
    [print(c) for c in candidates]
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
