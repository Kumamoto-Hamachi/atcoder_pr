import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def con1(a, b, c, d):
    if a + b == c + d:
        return True
    return False

def con2(a, b, c, d):
    if a - b == c - d:
        return True
    return False

def con3(a, b, c, d):
    if abs(a - c) + abs(b - d) <= 3:
        return True
    return False

def all_con(a, b, c, d):
    if con1(a, b, c, d) or con2(a, b, c, d) or con3(a, b, c, d):
        return True
    return False

def two_path_con(a, b ,c ,d):
    x = c - a
    y = d - b
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
        return True
    return False

def final(a, b, c, d):
    x = c
    y = (c - a) + b
    if abs((c - x) + (d - y)) == 1:
        return True
    return False

# wrong ans
if __name__ == "__main__":
    a, b = m_snput()
    c, d = m_snput()
    x = c - a
    y = d - b
    if a == c and b == d:
        print(0)
    elif all_con(a, b, c, d):
        print(1)
    elif two_path_con(a, b, c, d):
        print(2)
    elif final(a, b, c, d):
        print(2)
    else:
        print(3)

        """
    elif abs(c - d) <= 3:
        print(2)
        """
