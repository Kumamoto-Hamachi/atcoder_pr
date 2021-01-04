import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n = int(snput())
    suprised_prefix_set, not_prefix_set = set(), set()
    for _ in range(n):
        s = snput()
        if s[0] == "!":
            suprised_prefix_set.add(s[1:])
        else:
            not_prefix_set.add(s)
    intersection = suprised_prefix_set & not_prefix_set
    # try-except使いたくないなぁ
    try:
        print(intersection.pop())
    except:
        print("satisfiable")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
