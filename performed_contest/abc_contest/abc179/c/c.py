import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def count_ab(a_b):
    count = 0
    for i in range(1, a_b+1):
        count += a_b // i
    return count

if __name__ == "__main__":
    n = int(snput())
    abc_count = 0
    a_b = n - 1
    abc_count += count_ab(a_b)
    print(abc_count)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
