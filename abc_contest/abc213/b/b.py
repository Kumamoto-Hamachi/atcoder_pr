from pprint import pprint as pp
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]


if __name__ == "__main__":
    N = int(readline())
    a_list = list(map_readline())
    except_a = max(a_list)
    min_a = -1 * sys.maxsize
    for i, a in enumerate(a_list):
        if a != except_a and a > min_a:
            min_i = i
            min_a = a
    print(min_i + 1)

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    low_english_literature = " ".join(sreadlines())
    """
