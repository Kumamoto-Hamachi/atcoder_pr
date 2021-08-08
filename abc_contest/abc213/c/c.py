import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())


if __name__ == "__main__":
    h, w, n = map_readline()
    hw_l = [None] * n
    #h_l = [None] * n
    h_l = set()
    h_dict = {}
    #w_l = [None] * n
    w_l = set()
    w_dict = {}

    for i in range(n): # 10 ** 5
        a, b = map_readline()
        hw_l[i] = [a-1, b-1]
        h_l.add(a-1)
        w_l.add(b-1)
        #w_l[i] = b-1
        h_dict[a-1] = 1
        w_dict[b-1] = 1

    h_l = sorted(h_l)
    w_l = sorted(w_l)

    h_cnt = 0
    #print("h_dict", h_dict)  # debug
    #print("h_l", h_l)  # debug
    for a in h_l:
        cnt = h_dict[a]
        h_cnt += cnt
        h_dict[a] = a + 1 - h_cnt
    #print("h_dict", h_dict)  # debug

    w_cnt = 0
    #print("w_dict", h_dict)  # debug
    for a in w_l:
        cnt = w_dict[a]
        w_cnt += cnt
        w_dict[a] = a + 1 - w_cnt
    #print("w_dict", w_dict)  # debug

    for i, hw in enumerate(hw_l):
        h, w = hw
        h -= h_dict[h] - 1
        w -= w_dict[w] - 1
        print(h, w)
