import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    monster_num, special_attack_num = map_readline()
    monster_list = list(map_readline())
    monster_list.sort(reverse=True)
    fennec_cnt = sum(monster_list[special_attack_num:])
    print(fennec_cnt)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

