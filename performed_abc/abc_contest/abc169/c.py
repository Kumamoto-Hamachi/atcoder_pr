import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a, b = snput().split()
    a = int(a)
    # b = int(b.replace(".",""))
    b =  round(float(b) * 100)
    ans = a * b // 100
    print(ans)
    """
    a, b = int(a), int(float(b) * 100)
    b = 1.15のとき
    print(type(b), b) => 114になる
    """
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
