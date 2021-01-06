import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    n_list = [None] * n
    for i in range(n):
        n_list[i] = snput()
    n_set = set(n_list)
    print(len(n_set))
