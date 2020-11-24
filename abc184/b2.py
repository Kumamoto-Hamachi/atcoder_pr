def accept_one_row():
    input_list = input().strip().split()
    return input_list

def convert_list_mem_to_int(target_list):
    return list(map(int, target_list))

if __name__ == "__main__":
    input_list = accept_one_row()
    input_list = convert_list_mem_to_int(input_list)
    n, x = input_list
    circle_cross_list = input()
    for s in circle_cross_list:
        if s == "o":
            x += 1
        else:
            x = max(0, x-1)
    print(x)
