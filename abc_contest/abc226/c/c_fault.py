import sys
import math
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def list_readline(): return list(map_readline())


memo = [True] * (2 * 10 ** 5 + 1)
def collect(target_set):
    if target_set == set():
        return set()
    new_set = set()
    for num in target_set:
        if memo[num]:
            memo[num] = False
            new_set |= set(tech_infos[num-1])
    target_set |= collect(new_set)
    return target_set


if __name__ == "__main__":
    N = int(readline())
    tech_infos = [None] * N
    times = [None] * N
    for i in range(N):
        num_list = list_readline()
        tech_infos[i] = num_list[2:]
        times[i] = num_list[0]
    target = tech_infos[-1]
    first_target = set(target)
    ans_set = collect(first_target)
    ans = times[-1]
    for num in ans_set:
        ans += times[num-1]
    print(ans)
