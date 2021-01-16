import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    N = int(snput())
    num_list = list(m_snput())
    num_list.sort(reverse=True)
    left_side = [0] * N
    right_side = [0] * N
    for i in range(1, N):
        left_side[i] = num_list[i] * i
    for a, b in enumerate(range(N-1, 0, -1)):
        right_side[a] = num_list[a] * b
    ans = sum(right_side) - sum(left_side)
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
