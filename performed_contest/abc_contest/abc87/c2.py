import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# 実行時間は変わらないが綺麗な書き方
if __name__ == "__main__":
    n = int(snput())
    a_list = [list(m_snput()) for i in range(2)]
    candy_sum = 0
    for i in range(n):
        # ここの書き方参考に
        candy_sum = max(candy_sum, sum(a_list[0][:i+1]+a_list[1][i:]))
    print(candy_sum)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
