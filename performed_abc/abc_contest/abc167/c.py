import sys
import itertools
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def is_over_x(a_l, m, x, books_l):
    for i in range(1, m+1):
        tmp = 0
        for a in a_l:
            tmp += books_l[a][i]
        if tmp >= x:
            continue
        else:
            return False
    return True

def calc_sum(a_l, books_l):
    sum_p = 0
    for a in a_l:
        sum_p += books_l[a][0]
    return sum_p


# クソコードすぎる、書き直せ
if __name__ == "__main__":
    n, m, x = m_snput()
    n_l = [i for i in range(n)]
    books_l = [None] * n
    for i in range(n):
        books_l[i] = list(m_snput())
    # print("books_l", books_l)  # debug

    all_c = []
    for i in range(1, n+1):
        tmp_set = list(itertools.combinations(n_l, i))
        all_c += tmp_set
    # print("all_c", all_c)  # debug
    min_p = 10 ** 15 * 12 + 1
    for a_s in all_c:
        # print("a_s", list(a_s))  # debug
        a_l = list(a_s)
        if is_over_x(a_l, m, x, books_l):
            tmp_p = calc_sum(a_l, books_l)
            min_p = min(min_p, tmp_p)
    ans = min_p if min_p != 10 ** 15 * 12 + 1 else -1
    print(ans)


    """
    0
    1
    2
    01
    02
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
