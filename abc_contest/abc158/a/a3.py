import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def is_monopoly(stations):
    first = stations[0]
    for s in stations[1:]:
        if first != s:
            return False
    return True

if __name__ == "__main__":
    stations = snput()
    if is_monopoly(stations):
        print("No")
    else:
        print("Yes")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
