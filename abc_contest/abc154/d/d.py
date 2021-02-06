import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def calc_dice(num):
    expected_value = 0
    for i in range(1, num+1):
        expected_value += i
    expected_value /= num
    return expected_value


# この関数ひどい
def decide_max_list(p_l, N, K):
    max_len = N - K + 1
    max_list = [0] * max_len
    for i in range(K):
        max_list[0] += p_l[i]
    for i in range(1, max_len):
        # print("i", i)  # debug
        max_list[i] += (max_list[i-1] + (p_l[i-1+K] - p_l[i-1]))
    max_sum = max(max_list)
    for order, s in enumerate(max_list):
        if s == max_sum:
            return order


if __name__ == "__main__":
    N, K = map_readline()
    p_l = list(map_readline())
    num_l = [None] * K
    sum_n = 0
    order = decide_max_list(p_l, N, K)
    # print("order", order)  # debug
    for p in p_l[order:order+K]:
        # print("p", p)  # debug
        expected_value = calc_dice(p)
        sum_n += expected_value
    print(sum_n)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
