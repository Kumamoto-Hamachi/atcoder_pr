import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def m(some_list):
    sum_num = 0
    for i in some_list:
        sum_num += abs(i)
    return sum_num

def y(some_list):
    sum_num = 0
    for i in some_list:
        sum_num += (i ** 2)
    return math.sqrt(sum_num)

def c(some_list):
    some_list = list(map(abs, some_list))
    return max(some_list)

if __name__ == "__main__":
    n = int(snput())
    some_list = list(m_snput())
    ans_1 = m(some_list)
    print(ans_1)
    ans_2 = y(some_list)
    print(ans_2)
    ans_3 = c(some_list)
    print(ans_3)
