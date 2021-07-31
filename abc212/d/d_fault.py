import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":  # だめだめ
    Q = int(readline())
    records = [None] * Q
    knap = set()
    num_list = [0] * (Q + 1)
    for i in range(Q):
        query = list(map_readline())
        if query[0] == 1:
            knap.add(query[1])
        elif query[0] == 2:
            num_list[i] += query[1]
        else:
            tmp = min(knap)
            records[i] = tmp
            knap.remove(tmp)
        num_list[i+1] += num_list[i]
    for i in range(Q):
        if records[i] is not None:
            print(records[i] + num_list[i])
