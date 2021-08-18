import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()


def is_condition(condition, num_str):
    for con in condition:
        s, c = con
        if num_str[s-1] != c:
            return False
    return True


if __name__ == "__main__":
    n, m = map_readline()
    condition = [None] * m
    for i in range(m):
        s, c = list(map_readline())
        condition[i] = [s, str(c)]

    for num in range(1000):
        num = str(num)
        if len(num) != n:
            continue
        if is_condition(condition, num):
            print(num)
            sys.exit()
    print(-1)

    """ 解法1 非推奨(練習にはなる?)
    n, m = map_readline()
    target_number = [None] * n
    for _ in range(m):
        s, c = map_readline()
        if target_number[s-1] is None or target_number[s-1] == str(c):
            target_number[s-1] = str(c)
        else:
            print(-1)
            sys.exit()

    if target_number[0] == "0" and n > 1:
            print(-1)
            sys.exit()
    for i in range(n):
        if target_number[i] is None:
            if i == 0 and n > 1:
                target_number[i] = "1"
            else:
                target_number[i] = "0"
    target_number = "".join(target_number)
    print(target_number)
    """
