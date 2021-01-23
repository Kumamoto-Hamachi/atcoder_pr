import sys
from math import log, floor
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    N, K = m_snput()
    print(floor(log(N, K))+1)




    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
