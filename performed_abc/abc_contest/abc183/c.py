import sys
import itertools
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def count_time_k(k, all_path_time, zero_start):
    count = 0
    for z in zero_start:
        time = 0
        for i in range(len(z)-1):
            begin, goal = z[i], z[i+1]
            time += all_path_time[begin][goal]
        if time == k:
            count += 1
    return count

if __name__ == "__main__":
    n, k = m_snput()
    all_path_time = []
    for i in range(n):
        path_time = list(m_snput())
        all_path_time.append(path_time)
    # print("all_path_time", all_path_time)  # debug
    city_list = [i for i in range(n)]
    permutations_list = list(itertools.permutations(city_list, n))
    zero_start = []
    for i in  permutations_list:
        i = list(i)
        i.append(0)
        if i[0] == 0:
            zero_start.append(i)
    count = count_time_k(k, all_path_time, zero_start)
    print(count)
