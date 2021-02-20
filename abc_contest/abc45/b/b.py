from pprint import pprint as pp
from collections import defaultdict
import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def get_person(d, person, i):
    try:
        person = d[person][i]
    except:
        person = None
    return person

def judge_person(abc_list, len_list):
    for i in range(3):
        if abc_list[i] > len_list[i]:
            return i

# コードが長々しい。
if __name__ == "__main__":
    d = dict()
    person_l = ["A", "B", "C"]
    d["a"] = list(sreadline())
    d["b"] = list(sreadline())
    d["c"] = list(sreadline())
    person = "a"
    ai = 0
    a_len = len(d["a"])
    bi = 0
    b_len = len(d["b"])
    ci = 0
    c_len = len(d["c"])
    while True:
        # print("ai, bi, ci", ai, bi, ci)  # debug
        if person == "a":
            person = get_person(d, person, ai)
            ai += 1
        elif person == "b":
            person = get_person(d, person, bi)
            bi += 1
        elif person == "c":
            person = get_person(d, person, ci)
            ci += 1
        else:
            break
    abc_list = [ai, bi, ci]
    len_list = [a_len, b_len, c_len]
    winner_order = judge_person(abc_list, len_list)
    winner = person_l[winner_order]
    print(winner)

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
