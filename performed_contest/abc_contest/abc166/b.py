import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())


if __name__ == "__main__":
    n, k = m_snput()
    # sunuke_list = [i for i in range(1, n+1)]
    sunuke_set = set(i for i in range(1, n+1))
    sunuke_having_sweet_set = set()
    while True:
        try:
            d = int(snput())
            a_set = set(m_snput())
            # 論理演算
            sunuke_having_sweet_set |= a_set
        except:
            break
    # ここもう少し工夫できないか？
    """
    for i in sunuke_having_sweet_set:
        sunuke_list.remove(i)
    print(len(sunuke_list))
    """
    sunuke_set -= sunuke_having_sweet_set
    print(len(sunuke_set))



    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
