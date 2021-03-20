import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# ブサイクすぎる
def calc_two_expect(first, second):
    some_list = [first, second]
    some_abs_list = list(map(abs, some_list))
    max_1 = max(some_list)
    min_1 = min(some_list)
    max_2 = max(some_abs_list)
    min_2 = min(some_abs_list)
    if max_1 != max_2:
        max_2 = -1 * max_2
    if min_1 != min_2:
        min_2 = -1 * min_2
    return [max_1, max_2, min_1, min_2]

if __name__ == "__main__":
    a, b, c, d = m_snput()
    x_list = calc_two_expect(a, b)
    y_list = calc_two_expect(c, d)
    ans = -sys.maxsize
    for i in x_list:
        for n in y_list:
            if (i * n) > ans:
                ans = (i * n)
    print(ans)

