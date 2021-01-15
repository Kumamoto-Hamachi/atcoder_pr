import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    a_list = list(m_snput())
    mulitiplied_num = 1
    if 0 in a_list:
        print(0)
        sys.exit()
    for i in a_list:
        mulitiplied_num *= i
        if mulitiplied_num > 10 ** 18:
            print(-1)
            sys.exit()
    print(mulitiplied_num)
