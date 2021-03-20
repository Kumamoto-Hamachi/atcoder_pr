import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# 素因数分解
if __name__ == "__main__":
    n = int(snput())
    n_max = math.floor(math.sqrt(n))
    n_list = []
    for i in range(1, n_max+1):
        if n % i == 0:
            n_list.append(i)
            if n / i != i:
                n_list.append(int(n / i))
    n_list.sort()
    for i in n_list:
        print(i)

    """
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
    """

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
