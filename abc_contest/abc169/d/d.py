import sys
import math
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

def calc(N):
    arr = []
    limit = math.floor(N ** 0.5)
    for i in range(2, limit):
        if N % i == 0:
            arr.append(i)
            tmp = N // i
            if tmp != i:
                arr.append(tmp)
    return arr


def count(N, a):
    cnt = 0
    while True:
        if N % a == 0:
            cnt += 1
            N = N // a
        else:
            break
    return cnt, N

def count_tmp(tmp_cnt):
    additional = 0
    i = 1
    while True:
        if tmp_cnt > 0:
            tmp_cnt -= i
            if tmp_cnt < 0:
                break
            additional += 1
            i += 1
        else:
            break
    return additional


# 糞ブサイクなコード、直せ
if __name__ == "__main__":
    N = int(snput())
    arr = sorted(calc(N))
    if not arr and N != 1:
        print(1)
        sys.exit()
    cnt = 0
    for a in arr:
        tmp_cnt, N = count(N, a)
        cnt += count_tmp(tmp_cnt)
    print(cnt)
    """
    z = p ** e
    0 == N % z
    uqnique
    N = N // z
    max?つまりzは小さいほどいいのでは？
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
