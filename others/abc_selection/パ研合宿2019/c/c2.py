import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def calc_score(first, second, a_l, N):
    score = 0
    for i in range(N):
        tmp_score = max(a_l[i][first], a_l[i][second])
        score += tmp_score
    return score


if __name__ == "__main__":
    N, M = map_readline()
    a_l = [None] * N
    max_score = 0
    for i in range(N):
        a_l[i] = list(map_readline())
    for first in range(M-1):
        for second in range(first+1, M):
            score = calc_score(first, second, a_l, N)
            max_score = max(max_score, score)
    print(max_score)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
