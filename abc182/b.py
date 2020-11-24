def accept_one_num_row():
    num_list = list(map(int, input().strip().split()))
    return num_list

if __name__ == "__main__":
    input_num = int(input().strip())
    num_list = accept_one_num_row()
    max_num = max(num_list)
    max_count = 1
    almost_gdk = max_num
    for i in range(2, max_num + 1):
        count = 0
        for n in num_list:
            if n % i == 0:
                count += 1
                max_count = max(count, max_count)
        if count == max_count:
            almost_gdk = i
    print(almost_gdk)
