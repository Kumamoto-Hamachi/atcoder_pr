import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


# itertools.combinations(n_l, 2)
def make_couple_songs(M):
    pattern = calc_num1_C_num2(M, 2)
    couples = [None] * pattern
    order = 0
    for i in range(M-1):
        for j in range(i+1, M):
            couples[order] = [i, j]
            order += 1
    return couples


def calc_num1_C_num2(num1, num2):
    com = 1
    denominator = 1
    for i in range(num2):
        com *= (num1 - i)
        denominator *= (i + 1)
    return com // denominator


def judge_max_score_pattern(couples, song_l):
    max_score = 0
    for c in couples:
        # print("c", c)  # debug
        tmp_score = calc_score(c, song_l)
        max_score = max(max_score, tmp_score)
    return max_score


def calc_score(com, song_l):
    score = 0
    first, second = com
    for s in song_l:
        onegame_score = max(s[first], s[second])
        # print("onegame_score", onegame_score)  # debug
        score += onegame_score
    return score


if __name__ == "__main__":
    N, M = map_readline()
    couples = make_couple_songs(M)
    song_l = [None] * N
    for i in range(N):
        song_l[i] = list(map_readline())
    max_score = judge_max_score_pattern(couples, song_l)
    print(max_score)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
