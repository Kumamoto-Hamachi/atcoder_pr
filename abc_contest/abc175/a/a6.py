import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    w_s = snput()
    w_list = w_s.split("S")
    r_day = max(map(len, w_list))
    print(r_day)
