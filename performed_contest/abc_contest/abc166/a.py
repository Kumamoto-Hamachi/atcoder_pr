import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    title = snput()
    if title == "ABC":
        print("ARC")
    else:
        print("ABC")

