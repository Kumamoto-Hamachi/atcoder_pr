import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc_len_num(s, t):
    s_list = s.split(t)
    num = min(map(len, s_list))
    return len_num

def wrong_count(s_challenge, t):
    wc = 0
    for i, s in enumerate(s_challenge):
        # print(t[i], s)
        if t[i] != s:
            wc += 1
    return wc

# 汚すぎる、遅すぎる
if __name__ == "__main__":
    s = snput()
    t = snput()
    s_len = len(s)
    t_len = len(t)
    min_wrong = sys.maxsize
    for i in range(s_len-t_len+1):
        #print(s[i:i+t_len])
        s_challenge = s[i:i+t_len]
        wc = wrong_count(s_challenge, t)
        if min_wrong > wc:
            min_wrong = wc
    print(min_wrong)
