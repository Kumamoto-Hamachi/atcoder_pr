import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    stones = snput()
    s_d = {"W":0, "R":0}
    wr_count = {"W":0, "R":0}
    for s in stones:
        s_d[s] += 1
    ideal_stones = "R" * s_d["R"] + "W" * s_d["W"]
    for i in range(n):
        if ideal_stones[i] != stones[i]:
            wr_count[ideal_stones[i]] += 1
    count = max(wr_count["R"], wr_count["W"])
    print(count)


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
