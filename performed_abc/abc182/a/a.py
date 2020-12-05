from pprint import pprint as pp
from pprint import pformat as pf
from copy import copy

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

def calc_allowable_num(follower_num):
    return 2 * follower_num + 100

if __name__ == "__main__":
    two_list = convert_input_to_list()
    two_num_list = convert_list_mem_to_int(two_list)
    a, b = two_num_list
    allowable_num = calc_allowable_num(a)
    # print("allowable_num", allowable_num)  # debug
    print(allowable_num - b)
