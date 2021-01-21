import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, q = m_snput()
    s = snput()
    # print("s", s)  # debug
    s_list = [0] * n
    for i in range(1, n):
        s_list[i] = s.count("AC", i-1, i+1) + s_list[i-1]
    for i in range(q):
        l, r = m_snput()
        print(s_list[r-1] - s_list[l-1])

"""ダメな書き方
#これだと計算量N!になる、上のやりかたならN通りで済む
    for i in range(1, n):
        s_list[i] = s.count("AC", 0, i+1)
"""


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
