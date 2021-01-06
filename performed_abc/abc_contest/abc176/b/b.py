import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# pythonは多倍長整数を扱える -> 他のやり方も見ること
if __name__ == "__main__":
    n = int(snput())
    if n % 9 == 0:
        print("Yes")
    else:
        print("No")
