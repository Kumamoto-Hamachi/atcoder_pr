import sys
readline = sys.stdin.buffer.readline
def sreadline(): return readline().decode("utf-8").rstrip()


def count_trio(cadidates, firsts):
    cnt = 0
    cadidate_len = len(cadidates)
    for a in range(cadidate_len-2):
        for b in range(a+1, cadidate_len-1):
            for c in range(b+1, cadidate_len):
                af, bf, cf = firsts[a], firsts[b], firsts[c]
                cnt += cadidates[af] * cadidates[bf] * cadidates[cf]
    return cnt


if __name__ == "__main__":
    N = int(readline())
    cadidates = {}
    first_set = set()
    for _ in range(N):
        first = sreadline()[0]
        if first in ["M", "A", "R", "C", "H"]:
            cadidates.setdefault(first, 0)
            cadidates[first] += 1
            first_set.add(first)

    firsts = list(first_set)
    cnt = count_trio(cadidates, firsts)
    print(cnt)
