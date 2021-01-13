import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    lot, required = m_snput()
    ans = math.ceil(required / lot)
    print(ans)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
