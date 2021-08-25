from itertools import permutations
import sys
import math
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


def calc_travel_distance(idxes, town_list):
    town_num = len(town_list)
    travel_distance = 0
    for i in range(town_num-1):
        bef_i = idxes[i]
        af_i = idxes[i+1]
        bef_town = town_list[bef_i]
        af_town = town_list[af_i]
        travel_distance += calc_two_town(bef_town, af_town)
    return travel_distance


def calc_two_town(bef_town, af_town):
    distance_square = 0
    for b, a in zip(bef_town, af_town):
        distance_square += (a - b) ** 2
    distance = distance_square ** 0.5
    return distance


if __name__ == "__main__":
    town_num = int(readline())
    town_list = [None] * town_num
    for i in range(town_num):
        town_list[i] = list(map_readline())

    town_idxes = [i for i in range(town_num)]
    town_idxes_list = permutations(town_idxes)

    distance_sum = 0
    for idxes in town_idxes_list:
        distance_sum += calc_travel_distance(idxes, town_list)
    distance = distance_sum / math.factorial(town_num)
    print(distance)
