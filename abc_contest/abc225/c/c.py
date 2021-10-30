import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def list_readline(): return list(map_readline())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]


def not_match(start_b, b_grp, idx):
    for sb, b in zip(start_b, b_grp):
        if b != sb + 7 * i:
            return True
    return False


def make_mod_list(all_mod_list, b_grp):
    b_len = len(b_grp)
    flg = True
    for i, m in enumerate(all_mod_list):
        if m == b_grp[0] % 7:
            idx = i
            flg = False
            break
    if flg:
        return False
    if idx + b_len > 7:
        return False
    for i in range(b_len):
        if b_grp[i] % 7 != all_mod_list[idx+i]:
            return False
    return True


# modの発想
if __name__ == "__main__":
    all_mod_list = [i for i in range(1, 7)]
    all_mod_list.append(0)
    N, M = list_readline()
    b_grp = [None] * N
    for i in range(N):
        b_grp[i] = list_readline()
        if i == 0:
            flg = make_mod_list(all_mod_list, b_grp[i])
            start_b = b_grp[i]
            if not flg:
                print("No")
                sys.exit()
        else:
            if not_match(start_b, b_grp[i], i):
                print("No")
                sys.exit()
    print("Yes")
