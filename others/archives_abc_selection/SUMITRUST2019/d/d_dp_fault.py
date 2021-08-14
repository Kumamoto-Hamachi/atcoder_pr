import sys
from copy import copy
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


def boaring_method(N, S):
    original_pws = set()
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                pw = S[i] + S[j] + S[k]
                original_pws.add(pw)
    return original_pws


def make_pw(N, S, original_set):
    n_digit = 3 # 今見ている桁
    for d in range(n_digit, N):
        new_num = S[d]
        currents, original_set = create_new_pw(new_num, original_set)
        original_set |= set([c for c in currents if c is not None])
    return original_set


def create_new_pw(new, original_set):
    new_currents = [None] * len(original_set) * 2 * 3
    order = 0
    for c in original_set:
        for i in range(2):
            for j in range(i+1, 3):
                tmp = c[i] + c[j] + new
                if tmp not in original_set:
                    # new_currents.append(tmp)
                    new_currents[order] = tmp
                    order += 1
    return new_currents, original_set

# 正面突破[O(N**3)], えせ動的計画法[高々O(3 * 1000 * N)]、両方ともTLE
if __name__ == "__main__":
    N = int(readline())
    S = sreadline()
    original_set = {S[:3]} # set
    original_set = make_pw(N, S, original_set)
    print(len(original_set))
    """
    original_pws = boaring_method(N, S)
    print(len(original_pws))
    """
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

