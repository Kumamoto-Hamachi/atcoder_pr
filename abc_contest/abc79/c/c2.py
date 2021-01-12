import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def make_ans_str(bin_a, abcd):
    ans_str = ""
    bin_a = bin_a.replace("0", "-")
    bin_a = bin_a.replace("1", "+")
    for i, num in enumerate(abcd):
        ans_str += str(num)
        if i != 3:
            ans_str += bin_a[i]
    ans_str +=  "=7"
    return ans_str

# とてつもないクソコードなので後で直す
if __name__ == "__main__":
    abcd = list(map(int, list(snput())))
    for a in range(8): # 8
        ans = abcd[0]
        bin_a = bin(a)
        bin_a = bin_a[2:]
        bin_a_len = len(bin_a)
        if bin_a_len == 1:
            bin_a += "0" * (3 - bin_a_len)
            bin_a = bin_a[::-1]
        elif bin_a_len == 2:
            bin_a = "0" + bin_a
        for i, b in enumerate(bin_a): # 3
            if int(b):
                ans += abcd[i+1]
            else:
                ans -= abcd[i+1]
        if ans == 7:
            ans_str = make_ans_str(bin_a, abcd)
            print(ans_str)
            sys.exit()


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
