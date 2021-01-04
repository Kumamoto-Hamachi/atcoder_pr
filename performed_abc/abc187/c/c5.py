import sys

def snput():
    return sys.stdin.readline()

def divide_up(s, affiliation_set, opposite_set):
    if s in opposite_set:
        print(s)
        sys.exit()
    else:
        affiliation_set.add(s)
        return affiliation_set

if __name__ == "__main__":
    n = int(snput())
    prefix_mark_set = set()
    no_prefix_mark_set = set()
    for _ in range(n):
        s = snput()
        prefix = s[0]
        if prefix == "!":
            s = s[1:]
            prefix_mark_set = divide_up(s, prefix_mark_set, no_prefix_mark_set)
        else:
            no_prefix_mark_set = divide_up(s, no_prefix_mark_set, prefix_mark_set)
    print("satisfiable")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
