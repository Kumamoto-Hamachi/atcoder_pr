import sys
from math import gcd
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()
 

def lcm(list_l):
    greatest = max(list_l)
    i = 1
    while True:
        for j in list_l:
            if (greatest * i) % j != 0:
                i += 1
                break
        else:
            return greatest * i

def make_divisors(n):
    divisors = set()
    max_limit = int(n ** 0.5) + 1
    for i in range(1, max_limit):
        if n % i == 0:
            divisors.add(i)
            quotient = n // i
            if quotient != i:
                divisors.add(quotient)
    return divisors
 
 
if __name__ == "__main__":
    N, M = map_readline()
    a_list = list(map_readline())
    #greatest = lcm(a_list)
    greatest = 1
    for i in range(N):
        greatest *= a_list[i]
    g_div = make_divisors(greatest)
    g_set = set()
    for d in g_div:
        if d != 1 and d <= M:
            if d not in g_set:
                order = 1
                while True:
                   sce = d * order 
                   if sce > M:
                       break
                   g_set.add(sce)
                   order += 1
    M_set = set(range(1,M+1))
    M_set -= g_set
    M_list = sorted(list(M_set))
    print(len(M_list))
    for n in M_list:
        print(n)
