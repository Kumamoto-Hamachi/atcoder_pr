import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    k = int(snput())
    mod = 7
    cnt = 1
    for i in range(k):
        if mod % k == 0:
            break
        cnt += 1
        mod = (mod * 10 + 7) % k
    if mod % k == 0:
        print(cnt)
    else:
        print(-1)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
