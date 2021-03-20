import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    given_rate = 10 ** 9 + 7
    if n < 2:
        print(0)
        sys.exit()
    count = 0
    # 0以外
    count_without_0 = 9 ** n
    # 9以外
    count_without_9 = 9 ** n
    # 0と9以外
    count_without_0and9 = 8 ** n
    all_and_09= count_without_0 + count_without_9 - count_without_0and9
    all_sum = 10 ** n
    ans = all_sum - all_and_09
    ans %= given_rate
    print(ans)


    """
    0 ~ 9
    0も9も
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
