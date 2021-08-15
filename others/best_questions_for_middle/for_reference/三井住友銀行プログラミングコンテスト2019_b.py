import sys
import math
readline = sys.stdin.buffer.readline


if __name__ == "__main__":
    n = int(readline()) # nが50000以下なので50000まですべて試すやり方でも良い
    quotient = n / 1.08
    min_m = math.floor(quotient)
    max_m = math.ceil(quotient)
    if int(math.floor(min_m * 1.08)) == n:
        print(min_m)
    elif int(math.floor(max_m * 1.08)) == n:
        print(max_m)
    else:
        print(":(")
