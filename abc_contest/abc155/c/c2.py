import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    N = int(readline())
    vote_record = {}
    for _ in range(N):
        s = sreadline()
        if vote_record.get(s) is None:
            vote_record[s] = 0
        vote_record[s] += 1
    max_vote = 0
    candidate_list = []
    for v in vote_record.values():
        max_vote = max(max_vote, v)
    for k, v in vote_record.items():
        if v == max_vote:
            candidate_list.append(k)
    sorted_candidate_list = sorted(candidate_list)
    [print(c) for c in sorted_candidate_list]
    # [(print(c)) for c in sorted_candidate_list]
    # [print(f"{c}") for c in sorted_candidate_list]
    # [(print(f"{c}")) for c in sorted_candidate_list]
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
