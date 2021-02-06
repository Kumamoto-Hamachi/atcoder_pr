import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def is_vertex(h, w, points):
    cnt = 0
    for i in range(2):
        for j in range(2):
            # print("i, j", i, j)  # debug
            if points[h+i][w+j] == ".":
                cnt += 1
    if cnt % 2 == 1:
        return True
    return False

if __name__ == "__main__":
    H, W = map_readline()
    points = [None] * H
    for i in range(H):
        points[i] = list(sreadline())
    vertex_num = 0
    for h in range(H-1):
        for w in range(W-1):
            # print("h, w", h, w)  # debug
            if is_vertex(h, w, points):
                # print("cnt + ")
                vertex_num += 1
    print(vertex_num)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

