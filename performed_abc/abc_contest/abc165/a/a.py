import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# クソコード速攻直せ
if __name__ == "__main__":
    k = int(snput())
    a, b = m_snput()
    flag = False
    for i in range(a, b + 1):
        if i % k == 0:
            flag = True
    if flag == False:
        print("NG")
    else:
        print("OK")

