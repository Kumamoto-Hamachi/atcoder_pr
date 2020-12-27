import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    k, n = m_snput()
    a_list = list(m_snput())
    max_dist = 0
    for i in range(n):
        nxt = (i+1) % n
        distance = a_list[nxt] - a_list[i]
        if distance < 0:
            distance += k
        max_dist = max(max_dist, distance)
    print(k-max_dist)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
