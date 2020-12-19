import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    weather_s = snput()
    weather_l = weather_s.split("S")
    rain_d = max(map(len, weather_l))
    print(rain_d)
