from pprint import pprint as pp
from collections import defaultdict
import sys
import itertools
sys.setrecursionlimit(10 ** 7)
readlines = sys.stdin.buffer.readlines
map_readlines = lambda: map(int, readlines())
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def calc(com):
    tmp_sum = 0
    for c in com:
       tmp_sum += a_l[c]
    tmp_sum %= 200
    return tmp_sum

def get_ans(all_dict, N):
    for i in range(1, N):
        #print("i", i)  # debug
        if len(all_dict[i]) != len(set(all_dict[i])):
                inter = set(all_dict[i]) & set(all_dict[i])
                ans_set = [i, i, inter]
                return ans_set
        for j in range(i+1, N+1):
            #print("j", j)  # debug
            inter = set(all_dict[i]) & set(all_dict[j])
            if inter:
                ans_set = [i, j, inter]
                return ans_set
    return ["No", "No", "No"]

if __name__ == "__main__":
    N = int(readline())
    orders = list(range(N))
    #tmp_a_l = list(map_readline())
    a_l = list(map_readline())
    #a_l = [None] * len(tmp_a_l)
    """
    for i, a in enumerate(tmp_a_l):
        if a >= 200:
            add_num = a % 200
        else:
            add_num = 200 % a
        a_l[i] = add_num
    """
    #print("a_l", a_l)  # debug
    all_dict = {}
    all_com = []
    for i in range(1, N+1):
        com_l = list(itertools.combinations(orders, i))
        all_com.append(com_l)
        #print("com_l", com_l)  # debug
        all_dict[i] = [None] * len(com_l)
        for j, com in enumerate(com_l):
            tmp_sum = calc(com)
            all_dict[i][j] = tmp_sum
    #print("a_l", a_l)  # debug
    #print("all_dict", all_dict)  # debug
    ans_set = get_ans(all_dict, N)
    if ans_set[0] == "No":
        print("No")
        sys.exit()
    inter = list(ans_set[2])[0]
    a = ans_set[0]
    b = ans_set[1]
    #print("all_dict[a]", all_dict[a])  # debug
    flg = 0
    for i, n in enumerate(all_dict[a]):
        if n == inter:
            first = i
            #print("first", first)  # debug
            if a == b:
                flg = i
            break
    for i, n in enumerate(all_dict[b]):
        if i == flg:
            continue
        if n == inter:
            second = i
            #print("second", second)  # debug
            break
    first_line = sorted(list(all_com[a-1][first]))
    first_line = [str(i + 1) for i in first_line]
    first_line = [str(a)] + first_line
    second_line = sorted(list(all_com[b-1][second]))
    second_line = [str(i + 1) for i in second_line]
    second_line = [str(b)] + second_line
    first_line = " ".join(first_line)
    second_line = " ".join(second_line)
    print("Yes")
    print(first_line)
    print(second_line)
