import sys
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())

def calc_cosumed_energy(n, x_l):
    cosumed_energy = 0
    for x in x_l:
        cosumed_energy += (x - n) ** 2
    return cosumed_energy


if __name__ == "__main__":
    N = int(snput())
    x_l = list(m_snput())
    min_energy = 2 * (100 ** 2) * 100
    for n in range(101):
        min_energy = min(min_energy, calc_cosumed_energy(n, x_l))
    print(min_energy)
