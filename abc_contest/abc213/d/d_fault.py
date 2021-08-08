import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()
# return strs per line list
def sreadlines(): return [s.decode("utf-8").rstrip() for s in readlines()]



if __name__ == "__main__":
    n = int(readline())
    city_dict = {}
    for _ in range(n-1):
        a, b = map_readline()
        city_dict.setdefault(a, [])
        city_dict[a].append(b)
        city_dict.setdefault(b, [])
        city_dict[b].append(a)
    #print("city_dict", city_dict)  # debug

    place = 1
    arrived = [1]
    ideal = set([i for i in range(1, n+1)])
    arrived_record = {}
    while True:
        exists = False
        #print("place", place)  # debug
        for city in city_dict[place]:
            if city not in arrived:
                exists = True
                next_city = city
                arrived.append(next_city)
                arrived_record[next_city] = place
                break
        if not exists:
            place = arrived_record[place]
            arrived.append(place)
        else:
            place = next_city
            arrived.append(place)
        if place == 1 and set(arrived) == ideal:
            break
    print(arrived)
