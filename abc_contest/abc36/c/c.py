import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# なおせ
if __name__ == "__main__":
    n = int(snput())
    a_l = [None] * n
    for i in range(n):
        a_l[i] = int(snput())
    order_l = list(set(a_l))
    order_l.sort()
    order_dict = {}
    for i, a in enumerate(order_l):
        order_dict[a] = i
    for a in a_l:
        print(order_dict.get(a))
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
