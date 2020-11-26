import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# 他のやり方も検討すること
if __name__ == "__main__":
    n = int(snput())
    doublet_keyword = ""
    for i in range(n):
        d1, d2 = m_snput()
        if d1 == d2:
            doublet_keyword += "Y"
        else:
            doublet_keyword += "N"
    count_list = map(len, doublet_keyword.split("N"))
    if max(count_list) >= 3:
        print("Yes")
    else:
        print("No")
