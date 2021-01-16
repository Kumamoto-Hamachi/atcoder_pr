import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())
MAX = 2 * 10 ** 5 + 1

# これがd2.pyより早くなるの不思議！
if __name__ == "__main__":
    N, W = m_snput()
    all_time = [0] * MAX
    for _ in range(N):
        s, t, p = m_snput()
        all_time[s] += p
        all_time[t] -= p
    for i in range(MAX-1):
        all_time[i+1] += all_time[i]
    for t in all_time:
        if t > W:
            print("No")
            sys.exit()
    print("Yes")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
