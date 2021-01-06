import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    candy_list = [None] * 2
    for i in range(2):
        tmp_list = list(m_snput())
        candy_list[i] = tmp_list
    # print("candy_list", candy_list)  # debug
    max_candy = 0
    # ここもう少し美しく出来ないか？
    if n == 1:
        max_candy = candy_list[0][0] + candy_list[1][0]
        print(max_candy)
        sys.exit()
    for i in range(n+1):
        candy = sum(candy_list[0][:i]) + sum(candy_list[1][i-1:])
        max_candy = max(max_candy, candy)
    print(max_candy)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
