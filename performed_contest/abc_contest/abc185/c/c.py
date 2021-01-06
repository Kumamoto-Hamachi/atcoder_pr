import sys, math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    l = int(snput())
    l -= 12 # 先にボールを配り終わっておく
    l += 11 # 切り目を棒と考えて足す
    """
    l - 12 + 11 Combination 11(棒の置き場所)
    """
    com = 1
    for i in reversed(range(l + 1-11, l+1)):
        com *= i
    for i in range(1, 11+1):
        com //= i
    print(com)


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
