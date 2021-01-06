import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    x = int(snput())
    happiness = 0
    happiness += (x // 500) * 1000
    happiness += (x % 500) // 5 * 5
    print(happiness)
    """
    500:1000
    5:5
    500 * x + 5 * y + z = お金
    500 * x + 5 * y =  お金 - z
    500円を最大化、次点で5円を最大化
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
