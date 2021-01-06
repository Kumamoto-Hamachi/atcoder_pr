import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    h, w, k = m_snput()
    c = [0] * h
    for i in range(h):
        c[i] = snput()
    cnts = 0
    for rows in range(1 << h):
        for cols in range(1 << w):
            black = 0
            for i in range(h):
                if (rows >> i) % 2 == 1:
                    continue
                for j in range(w):
                    if (cols >> j) % 2 == 1:
                        continue
                    black += c[i][j] == "#"
            if black == k:
                cnts += 1
    print(cnts)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
