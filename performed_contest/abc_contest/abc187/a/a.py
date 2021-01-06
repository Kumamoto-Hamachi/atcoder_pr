import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc(s_l):
    tmp_sum = 0
    for s in s_l:
       tmp_sum += int(s)
    return tmp_sum

if __name__ == "__main__":
    a, b = m_snput()
    a_s = str(a)
    b_s = str(b)
    a_sum = calc(a_s)
    b_sum = calc(b_s)
    ans = a_sum if a_sum > b_sum else b_sum
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
