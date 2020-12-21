import sys
import itertools
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())


if __name__ == "__main__":
    n = int(snput())
    n_list = list(m_snput())
    n_list.sort(reverse=True)
    # print("n_list", n_list)  # debug
    sum_n = 0
    for i in range(n):
        left = n_list[i] * (n - i - 1)
        right = sum(n_list[i+1:])
        sum_n += (left - right)
    print(sum_n)

