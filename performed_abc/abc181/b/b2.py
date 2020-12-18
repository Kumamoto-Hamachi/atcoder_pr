import sys
snput = lambda: sys.stdin.readline().rstrip()

def sigma_func(a, b):
    num_length = b - a + 1
    sum_num = (a + b) * num_length // 2
    return sum_num


if __name__ == "__main__":
    n = int(snput())
    sum_num = 0
    for i in range(n):
        a, b = map(int, snput().split())
        sum_num += sigma_func(a, b)
    print(sum_num)
