import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def calc_match_diff_cnt(sign_stars, all_stars, tmp_origin, sign_star_num):
    cnt = 0
    for s in all_stars:
        if s != tmp_origin:
            x_diff = s[0] - tmp_origin[0]
            y_diff = s[1] - tmp_origin[1]
            if [x_diff, y_diff] in sign_stars:
                cnt += 1
    return cnt


if __name__ == "__main__":
    sign_star_num = int(readline())
    sign_stars = [None] * (sign_star_num - 1)
    origin_star = list(map_readline())
    for i in range(sign_star_num-1):
        x, y = map_readline()
        sign_stars[i] = [x - origin_star[0], y - origin_star[1]]
    all_star_num = int(readline())
    all_stars = [None] * all_star_num
    for i in range(all_star_num):
        all_stars[i] = list(map_readline())
    for tmp_origin in all_stars:
        cnt = calc_match_diff_cnt(sign_stars, all_stars, tmp_origin, sign_star_num)
        if cnt == sign_star_num - 1:
            true_origin = tmp_origin
            break
    print(true_origin[0] - origin_star[0], true_origin[1] - origin_star[1])

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
