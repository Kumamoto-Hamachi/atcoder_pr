import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    s_list = snput()
    t_list = snput()
    count = 0
    for i, s in enumerate(s_list):
        if s != t_list[i]:
            count += 1
    print(count)
