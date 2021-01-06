def accept_one_row():
    input_str = input().strip()
    input_list = input_str.split()
    return input_list

def convert_list_mem_to_int(target_list):
    return list(map(int, target_list))

if __name__ == "__main__":
    score_list = accept_one_row()
    score_list = convert_list_mem_to_int(score_list)
    N, X = score_list
    circle_and_cross = input().strip()
    for s in circle_and_cross:
        if s == "o":
            X += 1
        elif s == "x" and X >= 1:
            X -= 1
    print(X)

