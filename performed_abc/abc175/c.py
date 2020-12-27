import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc(k, min_try):
    k -= min_try
    k %= 2
    return k

# クソコード過ぎる
if __name__ == "__main__":
    x, k, d = m_snput()
    min_try = abs(x) // d
    if min_try >= k:
        if x >= 0:
            min_x = abs(x - d * k)
        else:
            min_x = abs(x + d * k)
        print(min_x)
        sys.exit()
    else:
        if x <= 0:
            x += (d * min_try)
            k = calc(k, min_try)
            x += d * k
        else:
            x -= (d * min_try)
            k = calc(k, min_try)
            x -= d * k
        print(abs(x))


    """
    for i in range(opt_c):
        for j in range(k-1, -1, -1):
            # print("i >> j", (i >> j) & 1)
            if ((i >> j) & 1):
                x += d
                print("hoge", x)
            else:
                x -= d
        print("x", x)  # debug
        min_x = min(min_x, abs(x))
    print(min_x)
    """

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
