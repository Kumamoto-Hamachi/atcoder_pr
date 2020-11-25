def accept_specified_rows(row_num):
    return [input().strip() for i in range(row_num)]
if __name__ == "__main__":
    input_list = accept_specified_rows(2)
    s, t = input_list
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")
