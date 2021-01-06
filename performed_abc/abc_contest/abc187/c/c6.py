import sys
snput = lambda: sys.stdin.readline().rstrip()
PREFIX = "!"


def add_without_opposite_partner(s, affiliation_set, opposite_set):
    if s in opposite_set:
        print(s)
        sys.exit()
    affiliation_set.add(s)
    return affiliation_set


if __name__ == "__main__":
    n = int(snput())
    mark_set = set()
    no_mark_set = set()
    for _ in range(n):
        s = snput()
        if s[0] == PREFIX:
            s = s[1:]
            mark_set = add_without_opposite_partner(s,
                                                    mark_set, no_mark_set)
        else:
            no_mark_set = add_without_opposite_partner(s,
                                                       no_mark_set, mark_set)
    print("satisfiable")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
