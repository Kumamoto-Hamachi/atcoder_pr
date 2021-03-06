import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
LIMIT = 45
memo = [0] * LIMIT


def fib(n):
    if n <= 1:
        return 1
    else:
        if memo[n] == 0:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


# メモ化再帰その2(グローバル変数の使用)
if __name__ == "__main__":
    N = int(readline())
    num = fib(N)
    print(num)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
