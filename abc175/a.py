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

def judge_and_update_max_num(max_num, challenge_num):
    if max_num <= challenge_num:
        max_num = challenge_num
    return max_num

# for Generic solving
if __name__ == "__main__":
    input_str = input().strip()
    c_flag = False
    r_day = 0
    max_day = 0
    for s in input_str:
        if s == "R" and c_flag == False:
            c_flag = True
            r_day = 1
        elif s== "R" and c_flag == True:
            r_day += 1
        else:
            c_flag = False
            max_day = judge_and_update_max_num(max_day, r_day)
            r_day = 0

    max_day = judge_and_update_max_num(max_day, r_day)
    print(max_day)
