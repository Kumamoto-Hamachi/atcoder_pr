from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
"""
def caracal_attack(monster_hitpoint, cnt):
    if monster_hitpoint == 1:
        cnt += 1
        return cnt
    monster_hitpoint //= 2
    return 2 * caracal_attack(monster_hitpoint, cnt)

"""

def caracal_attack(monster_hitpoint):
    cnt = 0
    cnt = mon(monster_hitpoint, cnt)
    return cnt

def mon(monster_hitpoint, cnt):
    for m in monster_hitpoint:
        if m == 1:
            cnt += 1
            monster_hitpoint.remove(m)
            if monster_hitpoint != []:
                cnt = mon(monster_hitpoint, cnt)
        else:
            monster_hitpoint.remove(m)
            cnt += 1
            m //= 2
            monster_hitpoint.append(m)
            monster_hitpoint.append(m)
            cnt = mon(monster_hitpoint, cnt)
    return cnt

if __name__ == "__main__":
    monster_hitpoint = list(map_readline())
    a = caracal_attack(monster_hitpoint)
    print(a)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

