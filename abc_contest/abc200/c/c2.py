import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())


def count_same(num):
    cnt = 0
    for i in range(1, num):
        cnt += i
    return cnt


if __name__ == "__main__":
    N = int(readline())
    a_l = list(map_readline())
    a_l = [i % 200 for i in a_l]  # 2 * 10 ** 5
    a_d = {}
    for a in a_l: # 2 * 10 ** 5
        a_d.setdefault(a, 0)
        a_d[a] += 1
    cnt = 0
    for v in a_d.values():  # 2 * 10 ** 5
        cnt += count_same(v)
    print(cnt)
