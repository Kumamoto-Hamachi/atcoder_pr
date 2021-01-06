import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    s_list = list(snput())
    flag = False
    count, max_count = (0, 0)
    for i in s_list:
        if i == "R" and flag == False:
            count += 1
            flag = True
        elif i == "R":
            count += 1
        else:
            flag = False
            if count >= max_count:
                max_count = count
            count = 0
    if count >= max_count:
        max_count = count
    print(max_count)
