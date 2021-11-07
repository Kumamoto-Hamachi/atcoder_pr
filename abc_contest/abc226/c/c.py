import sys
import math
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def list_readline(): return list(map_readline())


# curoaの解き方参考にした
# なぜ最初からsetを足していく馬鹿なやり方でなくこれにしないのか
# このやり方でも何度も間違えるのか, よく考えろ
def collect(target_set):
    if target_set == set():
        return set()
    new_set = set()
    for num in target_set:
        if not memo[num-1]:
            memo[num-1] = True
            new_set = set(tech_infos[num-1])
            collect(new_set)


if __name__ == "__main__":
    N = int(readline())
    tech_infos = [None] * N
    times = [None] * N
    for i in range(N):
        num_list = list_readline()
        tech_infos[i] = num_list[2:]
        times[i] = num_list[0]
    memo = [False] * N
    first_target = set(tech_infos[-1])
    collect(first_target)
    memo[-1] = True
    ans = 0
    for i, m in enumerate(memo):
        if m:
            ans += times[i]
    print(ans)
