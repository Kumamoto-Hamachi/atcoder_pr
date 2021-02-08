import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

def count_caracal_attack(cnt, H):
    if H == 1:
        cnt += 1
    else:
        H //= 2
        cnt += 1
        last_cnt = cnt
        cnt = count_caracal_attack(cnt, H)
        cnt += (cnt - last_cnt) # 増加分を計算することで二回計算する無駄を省く
    return cnt

if __name__ == "__main__":
    H = int(readline())
    cnt = 0
    cnt = count_caracal_attack(cnt, H)
    print(cnt)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

