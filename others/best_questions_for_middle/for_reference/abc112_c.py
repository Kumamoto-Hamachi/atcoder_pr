import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()


def is_correct_pyramid(X, Y, H, conditions):
    for con in conditions:
        x, y, h = con
        tmp_h = max((H - abs(x - X) - abs(y - Y)), 0)
        if tmp_h != h:
            return False
    return True


if __name__ == "__main__":
    n = int(readline())
    conditions = [None] * n
    for i in range(n):
        conditions[i] = list(map_readline())
    candidates = {}

    for con in conditions:
        x, y, h = con
        for xc in range(101):
            for yc in range(101):
                H = h + abs(x - xc) + abs(y - yc)
                candidates.setdefault((xc, yc), set())
                candidates[(xc, yc)].add(H)

    for center_xy, hc_set in candidates.items():
        xc, yc = center_xy
        for hc in hc_set:
            if is_correct_pyramid(xc, yc, hc, conditions):
                print(xc, yc, hc)
