import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    N = int(readline())
    total_score = 0
    min_not_ten_mulitiple_num = 101
    for _ in range(N):
        score = int(readline())
        total_score += score
        if score % 10 != 0:
            min_not_ten_mulitiple_num = min(min_not_ten_mulitiple_num, score)
    if total_score % 10 == 0:
        if min_not_ten_mulitiple_num != 101:
            total_score -= min_not_ten_mulitiple_num
        else:
            total_score = 0
    print(total_score)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
