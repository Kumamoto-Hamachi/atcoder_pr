import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# The official answer version
if __name__ == "__main__":
    w = snput()
    p = (w[0] == "R")
    q = (w[1] == "R")
    r = (w[2] == "R")
    if (p and q and r):
        print(3)
    elif (p and q) or (q and r):
        print(2)
    elif (p or q or r):
        print(1)
    else:
        print(0)
