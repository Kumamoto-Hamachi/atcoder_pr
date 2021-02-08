import sys
readline = sys.stdin.buffer.readline

def count_caracal_attack(H):
    if H == 1:
        return 1
    H //= 2
    cnt = 1 + 2 * count_caracal_attack(H)
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
