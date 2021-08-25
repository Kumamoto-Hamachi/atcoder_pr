from itertools import permutations
import sys
import math
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()


def is_ok(nl, n, path_list):
    for i in range(n-1):
        if not [nl[i], nl[i+1]] in path_list:
            return False
    return True


if __name__ == "__main__":
    n, m = map_readline()
    path_list = [None] * (m * 2)
    for i in range(m):
        path_list[i] = list(map_readline())
    for i in range(m):
        path_list[i+m] = path_list[i][::-1]

    
    # 1が起点なのでこういうことをしているが全部試す場合と時間変わらないみたい
    n_list = [i for i in range(2, n+1)]
    patterns = math.factorial(n-1)
    n_per_list = [None] * patterns
    n_pers = permutations(n_list)
    for i, nl in enumerate(n_pers):
        nl = [1] + list(nl)
        n_per_list[i] = nl


    cnt = 0
    for nl in n_per_list:
        nl = list(nl)
        #if nl[0] != 1:
        #    continue
        # print("nl", nl)  # debug
        if is_ok(nl, n, path_list):
            cnt += 1
    print(cnt)
