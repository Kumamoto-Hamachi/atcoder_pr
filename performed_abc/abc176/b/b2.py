import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())


# redundant approach(圧倒的に早い)
if __name__ == "__main__":
    n_s = snput()
    sum_num = 0
    for i in range(len(n_s)):
        sum_num += int(n_s[i])
    if sum_num % 9 == 0:
        print("Yes")
    else:
        print("No")
