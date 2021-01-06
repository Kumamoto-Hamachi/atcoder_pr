import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    at_d = {"AC":0,
            "WA":0,
            "TLE":0,
            "RE":0}
    for i in range(n):
        s = snput()
        at_d[s] += 1
    for k, v in at_d.items():
        print(k + " x " + str(v))



    """
    print(1+2+(3+4-5)+(6-7/8+9))
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
