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

def fetch_target_two_int():
    input_list = convert_input_to_list()
    input_list = convert_list_mem_to_int(input_list)
    target_1 , target_2 = input_list
    return target_1, target_2

if __name__ == "__main__":
    a, b = fetch_target_two_int()
    c, d = fetch_target_two_int()
    ans = a*d - b*c
    print(ans)
