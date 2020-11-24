def accept_one_row():
    input_list = input().strip().split()
    return input_list


def convert_list_mem_to_int(target_list):
    return list(map(int, target_list))

if __name__ == "__main__":
    input_list = accept_one_row()
    input_list = convert_list_mem_to_int(input_list)
    s_x, s_y, g_x, g_y = input_list
    rate = g_y / s_y
    sum_length = g_x - s_x
    left_lenght = sum_length / (rate + 1)
    print(left_lenght + s_x)
