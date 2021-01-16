import sys
import math
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())


def factorzation(N):
    fact_list = []
    limit = math.floor(N ** 0.5)
    for i in range(2, limit):
        if N % i == 0:
            fact_list.append(i)
            tmp = N // i
            if tmp != i:
                fact_list.append(tmp)
    return fact_list

"""
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
"""


def calc_div(N, num):
    cnt = 0
    while True:
        if N % num == 0:
            N //= num
            cnt += 1
        else:
            break
    return cnt, N


def calc_tmp_cnt(div_num):
    i = 0
    tmp_cnt = 0
    for i in range(1, div_num+1):
        div_num -= i
        if div_num < 0:
            return tmp_cnt
        tmp_cnt += 1
    return tmp_cnt


if __name__ == "__main__":
    N = int(snput())
    fact_list = sorted(factorzation(N))
    if N == 1:
        print(0)
    elif not fact_list:
        print(1)
    else:
        cnt = 0
        for num in sorted(fact_list):
            div_num, N = calc_div(N, num)
            cnt += calc_tmp_cnt(div_num)
        print(cnt)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
