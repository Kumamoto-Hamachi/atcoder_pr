import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    r = int(snput())
    circle_round = 2 * r * math.pi
    print(circle_round)
