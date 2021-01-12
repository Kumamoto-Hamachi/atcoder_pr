import sys
import math
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# ゴミコードすぎる
if __name__ == "__main__":
    n = int(snput())
    stones = snput()
    stone_d = {"W":0, "R":0}
    wr_c = 0
    w_c = 0
    wr_flag = False
    excellent_wr = 0
    for i, s in enumerate(stones):
        if s == "W":
            w_c += 1
            if i != n-1:
                if stones[i+1] == "R":
                    excellent_wr += 1
        if s == "R":
            if w_c:
                w_c -= 1
                wr_c += 1
    ans = excellent_wr // 2
    ans += (wr_c - (ans * 2))
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
