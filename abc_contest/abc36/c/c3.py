import sys
# snput = lambda: sys.stdin.readline()
snput = lambda: sys.stdin.buffer.readline()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, *a_l = map(int, sys.stdin.buffer.read().split())
    # setのままでも問題ないか？
    sorted_unique_a_list = sorted(list(set(a_l)))
    a_d = {a: i  for i, a in enumerate(sorted_unique_a_list)}
    # ans = map(a_d.get, a_l)
    # print("\n".join(map(str, map(a_d.get, a_l))))
    for a in map(a_d.get, a_l):
        print(a)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
