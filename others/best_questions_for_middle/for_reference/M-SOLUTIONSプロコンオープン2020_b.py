"""
import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]


if __name__ == "__main__":
    a, b, c = map_readline()
    k = int(readline())
    for ak in range(k+1):
        for bk in range(k+1):
            for ck in range(k+1):
                if ak + bk + ck != k:
                    continue
                if c * (2 ** ck) > b * (2 ** bk) > a * (2 ** ak):
                    print("Yes")
                    sys.exit()
    print("No")
"""

"""
import sys
import math
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


def judge_count(tmp_k, first, second):
    for i in [-1, 0, 1]:
        if first < second * (2 ** (tmp_k + i)):
            tmp_k += i
            if tmp_k < 0: # これ重要！
                tmp_k = 0
            return tmp_k


if __name__ == "__main__":
    a, b, c = map_readline()
    k = int(readline())

    abk = math.ceil(math.log2(a / b))
    abk = judge_count(abk, a, b)
    b = b * (2 ** abk)

    bck = math.ceil(math.log2(b / c))
    bck = judge_count(bck, b, c)

    if abk + bck <= k:
        print("Yes")
    else:
        print("No")
"""

a, b, c = map(int, input().split())
k = int(input())
 
cnt = 0
while a >= b:
    b *= 2
    cnt += 1
 
while b >= c:
    c *= 2
    cnt += 1
 
if cnt <= k:
    print("Yes")
else:
    print("No")
