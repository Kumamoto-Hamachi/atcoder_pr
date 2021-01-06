import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a_str = snput()
    min_sum = 37
    for i in range(2 ** 3):
        a_sum = int(a_str[0])
        ans = ""
        ans += a_str[0]
        for j in range(1, 4):
            if ((i >> j-1) & 1):
                # print(f"+ {a_str[j]}") # debug
                a_sum += int(a_str[j])
                ans += f"+{a_str[j]}"
            else:
                # print(f"- {a_str[j]}") # debug
                a_sum -= int(a_str[j])
                ans += f"-{a_str[j]}"
        if a_sum == 7:
            print(f"{ans}=7")
            sys.exit()


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
