import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

PREFIX = "!"


def add_affiliation_set(s, no_mark_set, mark_set, mark_flag):
    affiliation_set = mark_set if mark_flag else no_mark_set
    affiliation_set.add(s)


def check_opposite_partner(s, no_mark_set, mark_set, mark_flag):
    opposite_set = no_mark_set if mark_flag else mark_set
    return (s in opposite_set)


if __name__ == "__main__":
    n = int(snput())
    mark_set = set()
    no_mark_set = set()
    ans = ""
    for _ in range(n):
        s = snput()
        mark_flag = (s[0] == PREFIX)
        s = s[1:] if mark_flag else s
        if check_opposite_partner(s, no_mark_set, mark_set, mark_flag):
            ans = s
            break
        add_affiliation_set(s, no_mark_set, mark_set, mark_flag)
    ans = ans if ans else "satisfiable"
    print(ans)

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
