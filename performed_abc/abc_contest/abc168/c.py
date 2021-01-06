import sys
from math import cos, radians
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a, b, h, m = m_snput()
    m += h * 60
    a_angle = m * 0.5 % 360
    b_angle = m * 6 % 360
    dif_angle = abs(a_angle - b_angle)
    cos_a = cos(radians(dif_angle))
    ans = (a ** 2 + b ** 2 - 2 * a * b * cos_a) ** 0.5
    print(ans)
    """
    短針:0.5
    長針:6
    余弦定理:cosA = (b ** 2 + c ** 2 - a ** 2) / 2 * b * c
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
