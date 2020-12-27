import sys
from math import *
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def generate_prime_factors(n, n_max):
    for i in range(1, n_max + 1):
        if n % (i) == 0:
            yield i
            if n // (i) != i:
                yield int(n // (i))

def howmuchdiv(n, i): return (0 if n % i != 0 else(1+howmuchdiv(n//i, i)))
def isprime(n): return all([n%i!=0 for i in range(2, int(sqrt(n)+1))])
def factorize(n): return ((i,howmuchdiv(n,i)) for i in range(2, int(sqrt(n))+2) if n % i == 0 and isprime(i))
def factorize_patner(n, i): return (i if n // i != 3 else 3)



# 素因数分解にジェネレーター式を使うのは難しい
if __name__ == "__main__":
    print(int(sqrt(2021) + 2))
    factorize_patner(10, 2)

    for i in factorize(2021):
        print(i)
    """
    n = int(snput())
    n_max = math.floor(math.sqrt(n))
    gen = generate_prime_factors(n, n_max)
    for i in gen:
        print(i)
    """
    """
    while True:
        hoge = next(gen)
        print("hoge", hoge)  # debug
        if hoge == n_max:
            flag = 1
        elif flag == 1:
            break

    """


    """
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
    """

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
