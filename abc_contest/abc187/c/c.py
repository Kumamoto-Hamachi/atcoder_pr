import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    n_d = {}
    for i in range(n):
        s = snput()
        if s[0] == "!":
            n_d.setdefault(s[1:], True)
            if n_d[s[1:]] == False:
                print(s[1:])
                sys.exit()
        else:
            n_d.setdefault(s, False)
            if n_d[s] == True:
                print(s)
                sys.exit()
    print("satisfiable")

    """
    for i in range(n):
        input_str = snput()
        if input_str[0] == "!":
            tmp_str = input_str[1:]
        else:
            tmp_str = input_str
        if tmp_str not in n_l:
            n_l[i] = input_str
        else:
            if input_str not in n_l:
                print(tmp_str)
                sys.exit()
    print("satisfiable")
    """
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
