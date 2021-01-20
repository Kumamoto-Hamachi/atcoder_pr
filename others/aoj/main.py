import sys
import math
readlines = sys.stdin.buffer.readlines # 複数行全てリスト,各要素全てbyteになってるけどあくまでリスト！
map_readlines = lambda: map(int, readlines()) # 上を全てintにしたmap
readline = sys.stdin.buffer.readline # 一行スペース空きをbyteで取る 毎回\nがツイてくる、単品のnumを取るのに使おう
map_readline = lambda: map(int, readline().split()) #上の各要素をintにしたmap
sreadline = lambda: readline().decode("utf-8").rstrip() # 上の要素を文字列にして合体

if __name__ == "__main__":
    n = int(readline())
    n_l = list(map_readline())
    n_l = n_l[::-1]
    n_l = list(map(str, n_l))
    ns = " ".join(n_l)
    print(ns)



    """
    input_num = int(snput())
    some_map = m_snput()
    """
