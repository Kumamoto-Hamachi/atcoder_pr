import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

def make_combinations(n, n_l):
    combinations = [None] * calc_num1_C_num2(n, 3)
    order = 0
    for i in range(n-2):
        for j in range(1, n-1):
            for k in range(2, n-2):
                combinations[order] = [n_l[i], n_l[j], n_l[k]]
                order += 1
    return combinations

def calc_num1_C_num2(num1, num2):
    com = 1
    for i in range(num2):
        com *= (num1 - i)
        print("com", com)  # debug
    for i in range(1, num2+1):
        com //= i
    return com

if __name__ == "__main__":
    n, p = map_readline()
    n_l = [i for i in range(1, n+1)]
    combinations = make_combinations(n, n_l)
    print("combinations", combinations)  # debug
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
