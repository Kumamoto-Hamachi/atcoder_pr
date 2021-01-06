import sys
import itertools
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# 何度も読解に失敗している
if __name__ == "__main__":
    n = int(snput())
    if n < 3:
        print(0)
        sys.exit()
    some_list = list(m_snput())
    combination_list = list(itertools.combinations(some_list, 3))
    #print("combination_list", combination_list)  # debug
    triangle_count = 0
    for c_t in combination_list:
        a, b, c = c_t
        triangle_count+= ((a + b) > c and (b + c) > a and (c + a) > b) and (a != b)\
                and (a != b) and (b != c) and (c != a)
    print(triangle_count)
