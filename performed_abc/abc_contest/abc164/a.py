import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    sheep, wolf = m_snput()
    if wolf >= sheep:
        print("unsafe")
    else:
        print("safe")
