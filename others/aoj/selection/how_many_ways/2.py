import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


# itertools.combinations(n_l, 3)
def make_combinations(n, n_l):
    combinations = [None] * calc_num1Cnum2(n, 3)
    order = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                combinations[order] = [n_l[i], n_l[j], n_l[k]]
                order += 1
    return combinations


def calc_num1Cnum2(num1, num2):
    com = 1
    denominator = 1
    for i in range(num2):
        com *= (num1 - i)
        denominator *= (i + 1)
    com //= denominator
    return com


def count_com_sum_is_same_to_specified_num(combinations, specified_num):
    cnt = 0
    for c in combinations:
        if sum(c) == specified_num:
            cnt += 1
    return cnt


if __name__ == "__main__":
    while True:
        n, p = map_readline()
        if n == 0 and p == 0:
            break
        n_l = [i for i in range(1, n+1)]
        combinations = make_combinations(n, n_l)
        cnt = count_com_sum_is_same_to_specified_num(combinations, p)
        print(cnt)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
