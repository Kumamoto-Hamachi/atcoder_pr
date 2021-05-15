import sys
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    N = int(readline())
    all_mount = [None] * N
    all_hight = [None] * N
    for i in range(N):
        tmp = input().split(" ")
        all_mount[i] = tmp[0]
        all_hight[i] = tmp[1]
    all_hight = [int(h) for h in all_hight]
    second = sorted(all_hight, reverse=True)[1]
    for i, h in enumerate(all_hight):
        if second == int(h):
            print(all_mount[i])
            sys.exit()

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
