import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


if __name__ == "__main__":
    N = int(readline())
    S = sreadline()
    cnt = 0
    for i in range(1000):
        num = str(i)
        num = "0" * (3 - len(num)) + num
        order = 0
        for s in S:
            order += (num[order] == s)
            if order == 3:
                cnt += 1
                break
    print(cnt)


    """
    000 ~ 999
    N * (N - 1) * (N - 2) / (3 * 2 * 1)
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

