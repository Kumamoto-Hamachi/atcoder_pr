import sys
import math
readline = sys.stdin.buffer.readline


def count_2(num):
    is_divisible = False
    cnt = 0
    while not is_divisible:
        is_divisible = True
        if num % 2 == 0:
            is_divisible = False
            num //= 2
            cnt += 1
    return cnt


if __name__ == "__main__":
    n = int(readline())
    max_cnt = 0
    max_num = 1
    for i in range(1, n+1):
        tmp_cnt = count_2(i)
        if tmp_cnt > max_cnt:
            max_cnt = tmp_cnt
            max_num = i
    print(max_num)
