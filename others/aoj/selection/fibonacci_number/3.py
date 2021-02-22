import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


def fib(n):
    fib_sequence = [1] * (n+1) # fib_sequence[0] = 1, fib_sequence[1] = 1
    # fib_sequence[2]以降
    for i in range(2, n+1):
        fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]
    return fib_sequence


# 動的計画法
if __name__ == "__main__":
    N = int(readline())
    fib_sequence = fib(N)
    print(fib_sequence[N])

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

