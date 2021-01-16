import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    a, b = m_snput()
    assumed_ans = set()
    for i in range(2):
        print((a-i)/0.08)
        assumed_ans.add((a-i) / 0.08)
    for i in range(2):
        tmp = (b-i) / 0.1
        print("tmp", tmp)  # debug
        if tmp in assumed_ans:
            print(int(tmp))
            sys.exit()
    print(-1)


    """少数が絡むと途端にだめ
    floor(x * 0.08) = a
    a, a-1
    floor(x * 0.1) = b
    b, b-1
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
