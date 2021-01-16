import sys
import itertools
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def is_all_odd(sequence):
    for s in sequence:
        if int(s) % 2 == 0:
            return False
    return True

# 駄目
if __name__ == "__main__":
    sequence = snput()
    all_pattern = itertools.product(sequence, repeat=3)
    all_pattern_without_odd = [p for p in all_pattern if int(p[-1]) % 2 == 0]
    for i, p in enumerate(all_pattern_without_odd):
        p_num = int("".join(list(p)))
        if p_num % 8 == 0:
            print("Yes")
            sys.exit()
    print("No")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
