import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def count_caracal_attack(H):
    cnt = 0
    if H == 1:
        return 1
    else:
        H //= 2
        cnt += 1
        tmp_cnt = cnt
        cnt += count_caracal_attack(H)
        cnt += (cnt - tmp_cnt)
    return cnt


if __name__ == "__main__":
    H = int(readline())
    cnt = count_caracal_attack(H)
    print(cnt)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

