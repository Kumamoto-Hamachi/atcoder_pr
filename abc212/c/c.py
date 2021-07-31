import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


if __name__ == "__main__":
    n, m = map_readline()
    a_l = list(set(map_readline()))
    b_l = list(set(map_readline()))
    c_l = a_l[:]
    c_l.extend(b_l)
    c_set = set(c_l)

    if len(c_set) < len(c_l):
        print(0)
        sys.exit()
    del c_set

    c_l = sorted(c_l)
    c_dict = {}
    for c in c_l:
        c_dict[c] = None

    for a in a_l:
        c_dict[a] = True
    del a_l
    for b in b_l:
        c_dict[b] = False
    del b_l

    a = sys.maxsize
    b = -1 * (a)
    min_num = abs(a-b)
    for k in c_l:
        a = k if c_dict[k] else a
        b = b if c_dict[k] else k
        tmp = abs(a-b)
        min_num = min(min_num, tmp)
    print(min_num)
