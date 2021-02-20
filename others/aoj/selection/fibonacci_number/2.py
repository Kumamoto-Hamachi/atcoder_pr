import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
LIMIT = 45


def fib(order, memo):
    if order <= 1:
        return 1
    else:
        if memo[order] == 0:
            memo[order] = fib(order-1, memo) + fib(order-2, memo)
        return memo[order]

# メモ化再帰
if __name__ == "__main__":
    N = int(readline())
    memo = [0] * LIMIT
    ans = fib(N, memo)
    print(ans)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

