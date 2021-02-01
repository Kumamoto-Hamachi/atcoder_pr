import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


def is_illegal(num, positive_filters, negative_filters):
    for nf in negative_filters:
        if num % nf != 0:
            return False
    for pf in positive_filters:
        if num % pf == 0:
            return False
    return True


if __name__ == "__main__":
    N = int(readline())
    a_l = list(map_readline())
    negative_filters = [2,]
    positive_filters = [3, 5]
    """
    これでもやはり拡張性は低い
    例えば「3の倍数でかつ5で割った時2余るときはDENIED」のなどの条件を付け加えるのだるい
    """
    for a in a_l:
        if is_illegal(a, positive_filters, negative_filters):
            print("DENIED")
            sys.exit()
    print("APPROVED")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

