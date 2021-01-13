import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc(sequence):
    cnt_dict = {}
    for s in sequence:
        s = int(s)
        cnt_dict.setdefault(s, 0)
        cnt_dict[s] += 1
    return cnt_dict

def compare(ans_dict, try_dict):
    for k, v in try_dict.items():
        tpm = ans_dict.get(k)
        tpm = tpm if tpm else 0
        if tpm < v:
            return False
    return True

# Counterを使って書き直すこと
if __name__ == "__main__":
    sequence = snput()
    if len(sequence) <= 2:
        if int(sequence) % 8 == 0 or int(sequence[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        sys.exit()
    ans_dict = calc(sequence)
    all_patern = [8 * i + 104 for i in range(112)]
    for p in all_patern:
        p_l = list(str(p))
        try_dict = calc(p_l)
        if compare(ans_dict, try_dict):
            print("Yes")
            sys.exit()
    print("No")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
