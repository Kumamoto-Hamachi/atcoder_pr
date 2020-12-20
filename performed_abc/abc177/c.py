import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    given_rate = 10 ** 9 + 7
    n = int(snput())
    a_list = list(m_snput())
    cumulative_l = a_list[:]
    for i in range(n-2, -1, -1):
        cumulative_l[i] += cumulative_l[i+1]
    sum_n = 0
    for i in range(n-1):
        sum_n += a_list[i] * cumulative_l[i+1]
    print(sum_n % given_rate)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
