def accept_one_num_row():
    num_list = list(map(int, input().strip().split()))
    return num_list

"""This func is cause of TLE
def sigma_func(two_list):
    sum_num = 0
    for i in range(two_list[0], two_list[1] + 1):
        sum_num += i
    return sum_num
"""

def sigma_func(two_list):
    start_num, end_num = two_list
    num_length = end_num - start_num + 1
    sum_num = (start_num + end_num) * num_length // 2
    return sum_num


if __name__ == "__main__":
    n = int(input().strip())
    sum_num = 0
    for i in range(n):
        num_list = accept_one_num_row()
        sum_num += sigma_func(num_list)
    #print(int(sum_num))
    print(sum_num)


