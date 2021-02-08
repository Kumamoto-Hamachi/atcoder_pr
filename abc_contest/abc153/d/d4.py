import sys
import math
readline = sys.stdin.buffer.readline


# 1, 3, 7, 15 の階差が等比になってる数列
def calc_caracal_attack_cnt(height):
    attack_cnt = 1 + 2 * (2 ** (height - 1) - 1)
    return attack_cnt


if __name__ == "__main__":
    H = int(readline())
    height = math.floor(math.log2(H)) + 1
    attack_cnt = calc_caracal_attack_cnt(height)
    print(attack_cnt)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
