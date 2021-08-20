def convert_10_to_2(num):
    converted_num = ""
    while True:
        rest = num % 2
        #print("rest", rest)  # debug
        converted_num = str(rest) + converted_num
        num //= 2
        if num < 2:
            converted_num = str(num) + converted_num
            return int(converted_num)


if __name__ == "__main__":
    n = 5
    num = convert_10_to_2(n)
    print("num", num)  # debug
