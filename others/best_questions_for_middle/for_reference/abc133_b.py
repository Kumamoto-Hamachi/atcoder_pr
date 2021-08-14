import sys
import math
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


if __name__ == "__main__":
    n, d = map_readline()
    coordinates = [None] * n
    for i in range(n):
        coordinates[i] = list(map_readline())

    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            distance = 0
            for z in range(d):
                distance += (coordinates[i][z] - coordinates[j][z]) ** 2
            distance = distance ** 0.5
            # print("distance", distance)  # debug
            if distance == math.floor(distance):
                cnt += 1
    print(cnt)
