import sys
import math
readlines = sys.stdin.buffer.readlines # 複数行全てリスト,各要素全てbyteになってるけどあくまでリスト！
map_readlines = lambda: map(int, readlines()) # 上を全てintにしたmap
readline = sys.stdin.buffer.readline # 一行スペース空きをbyteで取る 毎回\nがツイてくる、単品のnumを取るのに使おう
map_readline = lambda: map(int, readline().split()) #上の各要素をintにしたmap
sreadline = lambda: readline().decode("utf-8").rstrip() # 上の要素を文字列にして合体
# read = sys.stdin.buffer.read # 複数行全てbyte、これはreadlinesと違ってリストにならない、ほぼ使わない
# read = sys.stdin.read # 複数行を複数行のまま文字列で取ってくる これはstr、使わない
# readline = sys.stdin.readline # 一行を文字列で、これはstr \nがツイてくる
# readlines = sys.stdin.readlines # 一行を文字列で、これもstr、毎度\nがツイてくる

if __name__ == "__main__":
    r = int(readline())
    c_area = r ** 2 * math.pi
    c_fence = 2 * r * math.pi
    print(c_area, c_fence)
