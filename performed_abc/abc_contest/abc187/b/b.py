import sys
import itertools
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc_tilt(point_com):
    tilt = abs((point_com[1][1] - point_com[0][1]) / (point_com[1][0] - point_com[0][0]))
    if tilt <= 1:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(snput())
    n_l = [None] * n
    for i in range(n):
        n_l[i] = list(m_snput())
    point_combinations = list(itertools.combinations(n_l, 2))
    ans = 0
    for point_com in point_combinations:
        if calc_tilt(point_com):
            ans += 1
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
