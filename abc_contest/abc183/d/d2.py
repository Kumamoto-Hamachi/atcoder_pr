import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())
MAX = 2 * 10 ** 5 + 1

if __name__ == "__main__":
    N, W = m_snput()
    all_time = [0] * MAX
    first = MAX
    last = 0
    # imos
    for _ in range(N):
        s, t, p = m_snput()
        all_time[s] += p
        all_time[t] -= p
        first = min(first, s)
        last = max(last, t)
    target_time = all_time[first:last+1]
    target_len = last - first + 1
    for i in range(target_len-1):
        target_time[i+1] += target_time[i]
    for t in target_time:
        if t > W:
            print("No")
            sys.exit()
    print("Yes")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
