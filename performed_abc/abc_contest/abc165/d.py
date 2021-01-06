import sys
from math import floor
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc_given_conditon(a, b, x):
    return floor(a * x / b) - a * floor(x / b)

if __name__ == "__main__":
    a, b, n = m_snput()
    if n < b:
        print(calc_given_conditon(a, b, n))
    else:
        print(calc_given_conditon(a, b, b-1))

    """そのままfor文回すだけでは計算量的にダメ
    max_num = 0
    for i in range(n+1):
        tmp_num = calc_given_conditon(a, b, i)
        max_num = max(max_num, tmp_num)
    print(max_num)

    """

    """
    floor(a * x / b) - a * floor(x / b)
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
