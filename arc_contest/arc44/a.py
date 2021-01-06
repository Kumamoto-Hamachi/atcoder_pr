import sys
from math import floor
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def is_primer(num):
    limit = floor(num ** 0.5)
    for i in range(2, limit+1):
        if num % i == 0:
            return False
    return True

def is_similar_primer(num):
    str_num = str(num)
    unit_digit = int(str_num[-1])
    sum_n = sum(map(int, str_num))
    if unit_digit % 2 == 1 and unit_digit != 5 and sum_n % 3 != 0:
        return True
    return False

if __name__ == "__main__":
    n = int(snput())
    if (is_primer(n) or is_similar_primer(n)) and n != 1:
        print("Prime")
    else:
        print("Not Prime")
    """
    n 素数、合成数(not素数)1の位が奇数かつ5でないかつ各桁の我が3で割り切れない
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
