import sys
from heapq import heappush, heappop
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())


if __name__ == "__main__":
    n = int(readline())
    s_list = list(map_readline())
    t_list = list(map_readline())
    time_set = t_list[:]
    records = [False] * n
    currents = [0] * n
    sunuke_time = [None] * n
    time_manager = {}
    time_manager2 = {}

    for i, t in enumerate(t_list):
        time_manager.setdefault(t, [])
        time_manager[t].append(i)

    while sum(records) != n:
        t = heappop(time_set)

        flg = True
        flg2 = True
        if t not in time_manager:
            flg = False
        if t not in time_manager2:
            flg2 = False

        if flg:
            person_idx = time_manager[t]
            for i in person_idx:
                records[i] = True
                currents[i] += 1
                if sunuke_time[i] is None:
                    sunuke_time[i] = t
                move_time = s_list[i]
                time_manager2.setdefault(move_time+t, [])
                time_manager2[move_time+t].append(i)
                heappush(time_set, move_time+t)

        if flg2:
            person_idx2 = time_manager2[t]
            for i in person_idx2:
                if currents[i] == 0:
                    continue
                j = (i+1) % n
                records[j] = True
                currents[j] += 1
                currents[i] -= 1
                sunuke_time[j] = t
                move_time = s_list[j]
                time_manager2.setdefault(move_time+t, [])
                time_manager2[move_time+t].append(j)
                heappush(time_set, move_time+t)

    for t in sunuke_time:
        print(t)
