import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
sreadline = lambda: readline().decode("utf-8").rstrip()


def disassemble(S, patterns, dismiss_order):  # MLEになるのでこのような解き方に
    for p in patterns:
        len_p = len(p)
        if S[dismiss_order:dismiss_order+len_p] == p:
            dismiss_order += len_p
            S, dismiss_order = disassemble(S, patterns, dismiss_order)
    return S, dismiss_order


if __name__ == "__main__":
    S = sreadline()[::-1]
    patterns = ["dreamer", "eraser", "dream", "erase"]
    patterns = [p[::-1] for p in patterns]
    dismiss_order = 0
    S, dismiss_order = disassemble(S, patterns, dismiss_order)
    if len(S) == dismiss_order:
        print("YES")
    else:
        print("NO")
