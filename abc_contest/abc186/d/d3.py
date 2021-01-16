import sys
snput = lambda: sys.stdin.buffer.readline()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, *a_l = map(int, sys.stdin.buffer.read().split())
    a_l.sort(reverse=True)
    left_side = [None] * (n - 1)
    right_side = [None] * (n - 1)
    for a in range(n-1):
        b = n - a - 1
        left_side[a] = a_l[a] * b
        right_side[a] = a_l[b] * b
    ans = sum(left_side) - sum(right_side)
    print(ans)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
