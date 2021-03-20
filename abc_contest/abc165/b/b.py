import sys, math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    x = int(snput())
    stock = 100
    year = 0
    while stock < x:
        # 問題文をよく読めば利子の時点で切り捨てされるとわかるはず((#･∀･)
        stock += stock // 100
        year += 1
    print(year)
    """
    x = int(snput())
    currnet_stock = 100
    year = 0
    while True:
        if currnet_stock >= x:
            break
        currnet_stock *= 1.01
        currnet_stock = math.floor(currnet_stock)
        # print("currnet_stock", currnet_stock)  # debug
        year += 1
    print(year)
    """
