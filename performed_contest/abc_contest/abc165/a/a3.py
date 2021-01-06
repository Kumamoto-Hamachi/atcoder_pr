import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# shortest
if __name__ == "__main__":
    k = int(snput())
    a, b = m_snput()
    print("OK" if b // k > (a - 1) // k else "NG")
