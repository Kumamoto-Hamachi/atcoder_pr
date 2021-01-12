import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    x, y = m_snput()
    min_p =min(x, y)
    max_p = max(x, y)
    if (max_p - min_p) < 3:
        print("Yes")
    else:
        print("No")
