if __name__ == "__main__":
    pencil_num = int(input().strip())
    num_of_ones_place = pencil_num % 10
    calling = ""
    if num_of_ones_place == 3:
        calling = "bon"
    elif num_of_ones_place in (2, 4, 5, 7, 9):
        calling = "hon"
    else:
        calling = "pon"
    print(calling)
