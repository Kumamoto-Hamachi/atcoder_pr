import sys
import math
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    N = int(snput())
    ans = math.ceil(N / 2)
    print(ans)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
