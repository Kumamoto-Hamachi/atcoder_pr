from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8")

if __name__ == "__main__":
    N = int(readline())
    voting_dict = defaultdict(int)
    for _ in range(N):
        k = sreadline().rstrip()
        voting_dict[k] += 1
    max_value = max(voting_dict.values())
    max_k_l = sorted([kv[0] for kv in voting_dict.items() if kv[1] == max_value])
    for k in max_k_l:
        print(k)



    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
