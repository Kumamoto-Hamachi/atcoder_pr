import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    ans = ""
    while True:
        n -= 1 #for 0 index
        order = n % 26 # 26 ** 1 * n + 26 ** 2 * m + ... 26 ** 10 * p + order(0~25)
        ans += chr(order + ord("a"))
        if n < 26:
            break
        n //= 26
    print(ans[::-1])

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
