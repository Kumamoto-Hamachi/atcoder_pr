from pprint import pprint as pp
from pprint import pformat as pf
from copy import copy
from math import floor, ceil

# 一行目の標準入力をリスト化
def convert_input_to_list():
    input_str = input().strip()
    input_list = input_str.split()
    return input_list

# リスト要素を全て数値化
def convert_list_mem_to_int(target_list):
    for i, s in enumerate(target_list):
        target_list[i] = int(s)
    return target_list

# リストの中身全部の型確認
def check_all_list_mem_type(target_list):
    for i, m in enumerate(target_list):
        print(f"No.{i}: {m}", type(m))

# Non-generic solving
if __name__ == "__main__":
    s = input().strip()
    r_day = 0
    if s[0] == "R" and s[1] == "R":
        if s[2] == "R":r_day = 3
        else:r_day = 2
    elif s[1] == "R" and s[2] == "R":
        r_day = 2
    elif not s == "SSS":
        r_day = 1
    print(r_day)
