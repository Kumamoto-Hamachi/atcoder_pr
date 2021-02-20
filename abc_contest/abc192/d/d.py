import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


def convert_base_to_10(string, base):
    num = 0
    for s in string:
        num *= base
        num += int(s)
    return num # int


if __name__ == "__main__":
    X = sreadline()
    M = int(readline())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        sys.exit()
    max_num = int(max(list(X)))
    d = max_num + 1
    top = 10 ** 18 + 1
    bottom = max_num
    while top - bottom > 1:
        mid = (top + bottom) // 2
        num = convert_base_to_10(X, mid)
        if num <= M:
            bottom = mid
        else:
            top = mid
    top -= d
    bottom -= max_num
    print(bottom)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

