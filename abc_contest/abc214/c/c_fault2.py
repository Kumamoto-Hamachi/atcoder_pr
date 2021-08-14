import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def map_readlines(): return map(int, readlines())
def sreadline(): return readline().decode("utf-8").rstrip()

def is_end(record_sunuke, n):
    if sum(record_sunuke) == n:
        return True
    return False

def ans(sunuke_time):
    for t in sunuke_time:
        print(t)


if __name__ == "__main__":
    n = int(readline())
    s_list = list(map_readline())
    t_list = list(map_readline())


    limit_time = max(max(s_list), max(t_list))
    current_sunuke = [False] * n
    record_sunuke = [False] * n
    sunuke_time = [None] * n
    time_manager = {}
    time_manager2 = {}

    for i, t in enumerate(t_list):
        time_manager.setdefault(t, [])
        time_manager[t].append(i)

    for t in range(1, limit_time+1):
        #print("t", t)  # debug
        flg = True
        flg2 = True
        if t not in time_manager:
            flg = False
        if t not in time_manager2:
            flg2 = False

        if flg:
            person_idx = time_manager[t]
            for i in person_idx:
                record_sunuke[i] = True
                current_sunuke[i] = True
                if sunuke_time[i] is None:
                    sunuke_time[i] = t
                move_time = s_list[i]
                time_manager2.setdefault(move_time+t, [])
                time_manager2[move_time+t].append(i)

        if flg2:
            person_idx2 = time_manager2[t]
            for i in person_idx2:
                j = (i+1) % n
                record_sunuke[j] = True
                current_sunuke[j] = True
                current_sunuke[i] = False
                sunuke_time[j] = t
                move_time = s_list[j]
                time_manager2.setdefault(move_time+t, [])
                time_manager2[move_time+t].append(j)

        if is_end(record_sunuke, n):
            ans(sunuke_time)
            sys.exit()
