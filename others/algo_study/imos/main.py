import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    N = 7
    data = [0] * N
    order_num = int(snput())
    for _ in range(order_num):
        l, r, add = m_snput()
        print("l, r, add", l, r, add)  # debug
    """
    imos法:ある連続する空間に、ある数vを足す
    https://takeg.hatenadiary.jp/entry/2019/08/28/213526
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
