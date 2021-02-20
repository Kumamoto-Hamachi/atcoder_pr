import sys
readline = sys.stdin.buffer.readline

def count_caracal_attack(cnt, H):
    cnt += 1 # Hが何でも関係なく一度は攻撃カウント増える
    if H != 1:
        H //= 2
        tmp_cnt = cnt
        cnt = count_caracal_attack(cnt, H)
        cnt += (cnt - tmp_cnt)
    return cnt

if __name__ == "__main__":
    H = int(readline())
    cnt = 0
    cnt = count_caracal_attack(cnt, H)
    print(cnt)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
