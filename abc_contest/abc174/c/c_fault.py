import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    k = int(snput())
    num = 7
    cnt = 1
    for _ in range(k):
        if num % k == 0:
            break
        num += 7 * 10 ** cnt
        cnt += 1
    if num % k == 0:
        print(cnt)
    else:
        print(-1)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
