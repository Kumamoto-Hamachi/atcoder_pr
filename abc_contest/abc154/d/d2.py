import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def calc_expected_value(num):
    sum_num = 0
    for i in range(1, num+1):
        sum_num += i
    expected_value = sum_num / num
    return expected_value


def calc_max_expected_value(various_dices, dice_num, choice_num):
    order = judge_order(various_dices, dice_num, choice_num)
    max_expected_value = 0
    for num in various_dices[order:order+choice_num]:
        max_expected_value += calc_expected_value(num)
    return max_expected_value


def judge_order(various_dices, dice_num, choice_num):
    K_sum_list = make_sum_of_K_dices_list(various_dices, dice_num, choice_num)
    max_sum = max(K_sum_list)
    for order, K_sum in enumerate(K_sum_list):
        if K_sum == max_sum:
            return order


def make_sum_of_K_dices_list(various_dices, dice_num, choice_num):
    K_sum_list_len = dice_num - choice_num + 1
    K_sum_list = [0] * K_sum_list_len
    K_sum_list[0] = sum([various_dices[i] for i in range(choice_num)])
    for d, k in enumerate(range(1, K_sum_list_len)):
        K_sum_list[k] += (K_sum_list[k-1] - various_dices[d] + various_dices[d + choice_num])
    return K_sum_list


if __name__ == "__main__":
    dice_num, choice_num = map_readline()
    various_dices = list(map_readline())
    max_expected_value = calc_max_expected_value(various_dices, dice_num, choice_num)
    print(max_expected_value)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
