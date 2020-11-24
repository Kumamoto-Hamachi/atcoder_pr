def accept_one_num_row():
    num_list = list(map(int, input().strip().split()))
    return num_list

if __name__ == "__main__":
    num_list = accept_one_num_row()
    a, b = num_list
    print(a * b)
