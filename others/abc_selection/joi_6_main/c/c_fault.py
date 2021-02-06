import sys
from copy import copy
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

def all_search(pillar_num, pillar_coordinates):
    max_area = 0
    for a in range(pillar_num):
        for b in range(a+1, pillar_num):
            for c in range(b+1, pillar_num):
                for d in range(c+1, pillar_num):
                    # print("a,b,c,d", a,b,c,d)  # debug
                    first = calc_vector(pillar_coordinates[b], pillar_coordinates[a])
                    second = calc_vector(pillar_coordinates[c], pillar_coordinates[a])
                    third = calc_vector(pillar_coordinates[d], pillar_coordinates[a])
                    torio = [first, second, third]
                    points = [pillar_coordinates[a], pillar_coordinates[b], pillar_coordinates[c], pillar_coordinates[d]]
                    if is_square(torio, points):
                        tmp_area = calc_square(torio)
                        max_area = max(max_area, tmp_area)
    return max_area


def calc_square(torio):
    area_candidates = [None] * 3
    for i in range(3):
        area_candidates[i] = torio[i][0] ** 2 + torio[i][1] ** 2
    area_candidates.sort()
    if area_candidates[0] == area_candidates[1]:
        return area_candidates[0]
    else:
        return area_candidates[1]


def calc_vector(goal, start):
    vector = [None] * 2
    for i in range(2):
        vector[i] = goal[i] - start[i]
    return vector


def calc_point(start, move):
    for i in range(2):
        start[i] += move[i]
    return start


def is_square(torio, points):
    for a in range(3):
        for b in range(a+1, 3):
            # print("a,b", a,b)  # debug
            inner_product = torio[a][0] * torio[b][0] + torio[a][1] * torio[b][1]
            if inner_product == 0:
                for i in range(3):
                    if i != a and i != b:
                        rest_point = copy(points[i+1])
                        break
                ideal_point = copy(points[0])
                ideal_point = calc_point(ideal_point, torio[a])
                ideal_point = calc_point(ideal_point, torio[b])
                if rest_point == ideal_point:
                    return True


# 本コードのように正面から全探索するとPyPyでもTLE及びメモリ超過となる
if __name__ == "__main__":
    pillar_num = int(readline())
    pillar_coordinates = [None] * pillar_num
    for i in range(pillar_num):
        pillar_coordinates[i] = list(map_readline())
    max_area = all_search(pillar_num, pillar_coordinates)
    print(max_area)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
