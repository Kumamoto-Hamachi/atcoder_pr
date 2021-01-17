import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())
 
def calc(n, x_l):
    tmp = 0
    for x in x_l:
        tmp += (x - n) ** 2
    return tmp
 
 
if __name__ == "__main__":
    N = int(snput())
    x_l = list(m_snput())
    min_num = 2 * (100 ** 2)
    for n in range(0, 101):
        min_num = min(min_num, calc(n, x_l))
    print(min_num)
