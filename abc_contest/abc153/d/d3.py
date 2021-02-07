import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def calc_log2(num):
    power_of_2 = 0
    while num > 0:
        num //= 2
        power_of_2 += 1
    return power_of_2


def calc_attack_cnt(height): # 等比数列の和の公式
    attack_cnt = 1 + 2 ** height -2
    return attack_cnt


if __name__ == "__main__":
    H = int(readline())
    height = calc_log2(H) # これはmath使ってもいいか？
    attack_cnt = calc_attack_cnt(height)
    print(attack_cnt)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

