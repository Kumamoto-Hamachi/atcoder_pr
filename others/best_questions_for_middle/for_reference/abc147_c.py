import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


def make_person_tesimony(n):
    persons = [None] * n
    for i in range(n):
        speak_num = int(readline())
        speaks = [None] * speak_num
        for j in range(speak_num):
            speaks[j] = list(map_readline())
        persons[i] = speaks
    return persons


def is_valid_pattern(pattern, n, persons):
    bin_pattern = make_bit_pattern(pattern, n)
    for i in range(n-1, -1, -1):
        if (pattern >> i) & 1:
            if not is_all_speack_reliable(persons[n-1-i], bin_pattern): # TODO
                return False
    return True


def make_bit_pattern(pattern, n):
    bin_pattern = bin(pattern)[2:]
    bin_pattern = (n - len(bin_pattern)) * "0" + bin_pattern
    return bin_pattern


def is_all_speack_reliable(speaks, bin_pattern):
    #print("bin_pattern", bin_pattern)  # debug
    for speak in speaks:
        person_idx, state = speak
        #print("speak", speak)  # debug
        if int(bin_pattern[person_idx-1]) != state:
            return False
    return True


if __name__ == "__main__":
    n = int(readline())
    persons = make_person_tesimony(n)

    patterns = 2 ** n
    max_cnt = 0
    for pattern in range(patterns):
        if is_valid_pattern(pattern, n, persons):
            bin_pattern = make_bit_pattern(pattern, n)
            max_cnt = max(max_cnt, bin_pattern.count("1"))
    print(max_cnt)

""" 深さ優先探索と二重配列
import sys
readline = sys.stdin.buffer.readline

if __name__ == "__main__":
    n = int(readline())
    a = [0] * n
    x = [[0] * n for i in range(n)]
    y = [[0] * n for i in range(n)]
     
    for i in range(n):
        a[i] = int(input())
        for j in range(a[i]):
            x[i][j], y[i][j] = map(int, input().split())
            x[i][j] -= 1
     
     
    def check(honest):
        for i in range(n):
            if not honest[i]:continue
            for j in range(a[i]):
                if y[i][j] == 1 and not honest[x[i][j]]:return False
                if y[i][j] == 0 and honest[x[i][j]]:return False
        return True
            
    def dfs(honest):
        if len(honest) == n:
            if check(honest):
                return sum(honest)
            else:
                return 0
        return max(dfs(honest + [True]),
                   dfs(honest + [False]))
        
    print(dfs([]))
"""

""" 別解2 boolean_listの扱いをよく間違える.そこから自分の弱点を自覚しろ.
import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()


def collect_targets_and_states(n):
    targets = [[None] * n for i in range(n)]
    states = [[None] * n for i in range(n)]
    for i in range(n):
        speak_num = int(readline())
        for j in range(speak_num):
            targets[i][j], states[i][j] = map_readline()
            targets[i][j] -= 1  # because index starts from not 1 but 0
    return targets, states


def make_boolean_list(num, n):
    bin_num = bin(num)[2:]
    bin_num = (n - len(bin_num)) * "0" + bin_num
    boolean_list = list(map(int, bin_num))
    boolean_list = boolean_list[::-1]
    return boolean_list


def is_valid_pattern(boolean_list, n, targets, states):
    for i in range(n):
        if (p >> i) & 1:
            if not is_valid_speak(boolean_list, i, targets, states):
                return False
    return True


def is_valid_speak(boolean_list, idx, targets, states):
    for t, s in zip(targets[idx], states[idx]):
        if t is None and s is None:
            continue
        if boolean_list[t] != s:
            # print(boolean_list, idx, targets[idx]) # debug
            return False
        # else:
            # print("idx", idx)  # debug
            # print("targets", targets)  # debug
            # print("states", states)  # debug
            # print("boolean_list", boolean_list)  # debug
            # print("boolean_list[t]", boolean_list[t])  # debug
            # print("s", s, t)  # debug
    # print("boolean_list", boolean_list, targets, states)  # debug
    return True


if __name__ == "__main__":
    n = int(readline())
    targets, states = collect_targets_and_states(n)

    patterns = 2 ** n
    max_cnt = 0
    for p in range(patterns):
        boolean_list = make_boolean_list(p, n)  # TODO
        if is_valid_pattern(boolean_list, n, targets, states):
            max_cnt = max(max_cnt, sum(boolean_list))
    print(max_cnt)
