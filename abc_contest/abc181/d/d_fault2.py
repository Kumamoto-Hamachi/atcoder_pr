import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

# うんちコード
if __name__ == "__main__":
    sequence = snput()
    if len(sequence) <= 2:
        if int(sequence) % 8 == 0:
            print("Yes")
        else:
            print("No")
        sys.exit()
    sequence = list(sequence)
    all_p = [104 + 8 * i for i in range(112)]
    sequence = list(sequence)
    for n in all_p:
        n_s = str(n)
        tmp_dir = {}
        for s in n_s:
            tmp_dir.setdefault(s, 0)
            tmp_dir[s] += 1
        for s in n_s:
            print("s", s)  # debug
            if tmp_dir[s] != sequence.count(s):
                break
        print("Yes")
        sys.exit()
    print("No")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
