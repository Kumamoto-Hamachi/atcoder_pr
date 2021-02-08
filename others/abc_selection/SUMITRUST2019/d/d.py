import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    N = int(readline())
    S = sreadline()
    pins = [None] * 1000
    for i in range(1000):
        num = str(i)
        pins[i] = ("0" * (3- len(num))) + num
    cnt = 0
    for p in pins:
        order = 0
        for s in S:
            order += (p[order] == s)
            if order == 3:
                cnt += 1
                break
    print(cnt)


    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
