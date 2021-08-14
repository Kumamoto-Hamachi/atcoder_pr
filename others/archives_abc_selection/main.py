import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a = int(snput())
    b, c = m_snput()
    s = snput()
    print(a + b + c, s)
