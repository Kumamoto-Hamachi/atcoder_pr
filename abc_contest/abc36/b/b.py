import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    square = [None] * n
    new_square = [None] * n
    for i in range(n):
        square[i] = list(snput())
    for a in range(n):
        tmp = [None] * n
        for i, b in enumerate(range(n-1, -1, -1)):
            tmp[i] = square[b][a]
        new_square[a] = tmp
    for mark in new_square:
        mark_s = "".join(mark)
        print(mark_s)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
