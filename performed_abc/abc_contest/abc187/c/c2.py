import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    s_dict = {}
    # ifのなかにifあってブサイクかも
    for _ in range(n):
        s = snput()
        if s[0] == "!":
            tmp_value = s_dict.get(s[1:])
            if tmp_value == True or tmp_value is None:
                s_dict[s[1:]] = True
            else:
                print(s[1:])
                sys.exit()
        else:
            tmp_value = s_dict.get(s)
            if tmp_value == False or tmp_value is None:
                s_dict[s] = False
            else:
                print(s)
                sys.exit()
    print("satisfiable")
