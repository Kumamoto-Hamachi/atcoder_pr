import sys
# snput = lambda: sys.stdin.readline()
snput = lambda: sys.stdin.buffer.readline()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, *a_l = map(int, sys.stdin.buffer.read().split())
    unique_a_list = sorted(list(set(a_l)))
    order_d = {}
    for i, a in enumerate(unique_a_list):
        order_d[a] = i
    for a in a_l:
        print(order_d[a])

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
