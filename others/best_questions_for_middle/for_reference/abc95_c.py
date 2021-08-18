import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()


if __name__ == "__main__":
    a, b, c, x, y = map_readline()
    min_cost = a * x + b * y
    max_c_pizza = max(x, y) * 2

    min_idx = 0
    for i in range(0, max_c_pizza+1, 2):
        rest_x = max(x - (i // 2), 0)
        rest_y = max(y - (i // 2), 0)
        tmp_cost = a * rest_x + b * rest_y + c * i
        if tmp_cost < min_cost:
            min_idx = i
            min_cost = tmp_cost
    print(min_cost)
