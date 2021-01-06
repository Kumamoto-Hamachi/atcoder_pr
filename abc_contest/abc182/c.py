from copy import copy

import sys
import itertools

snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def delete_digit(n_list, n_len, s_num):
    order_list = [i for i in range(n_len)]
    delted_digit_order_list = set(itertools.combinations(order_list, s_num))
    all_copy_order = []
    for order_set in delted_digit_order_list:
        copy_order_list = copy(order_list)
        for i in order_set:
            copy_order_list.remove(i)
        all_copy_order.append(copy_order_list)
    return all_copy_order

def is_3_divided(n_list, all_order_list):
    for o_list in all_order_list:
        try_str = ""
        for i in o_list:
            try_str += n_list[i]
        try_num = int(try_str)
        if try_num % 3 == 0:
            return True
    return False

# 汚すぎる、時間かかりすぎ
if __name__ == "__main__":
    n = snput()
    n_list = list(map(str, [i for i in n]))
    n_len = len(n_list)
    if int(n) % 3 == 0:
        print(0)
        sys.exit()
    elif n_len == 1:
        print(-1)
        sys.exit()
    delete_digit(n_list, n_len, 3)
    for i in range(1, n_len):
        all_order_list = []
        all_order_list = delete_digit(n_list, n_len, i)
        if is_3_divided(n_list, all_order_list):
            print(i)
            sys.exit()
    print(-1)
