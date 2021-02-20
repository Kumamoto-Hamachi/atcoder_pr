import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def fib(order):
    if order == 0 or order == 1:
        return 1
    else:
        return fib(order-1) + fib(order-2)


# TLEになる => 動的計画法を使え
if __name__ == "__main__":
    N = int(readline())
    num = fib(N)
    print(num)
    """
    1 1 2 3 5
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

