import sys
snput = lambda: sys.stdin.readline()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, m, t = m_snput()
    max_n = n
    time_list = [True] * t

    for i in range(m):
        a, b = m_snput()
        for i in range(a, b):
            time_list[i] = False

    for i in time_list:
        if not i:
            if n != max_n:
                n += 1
        else:
            n -= 1
        if n <= 0:
            print("No")
            sys.exit()
    print("Yes")




    """
    n, m, t = m_snput()
    max_n = n
    cafe_list = [None] * m
    for i in range(m):
         cafe_list[i] = list(m_snput())
    count = 0
    for i in range(1, t*2+1):
        current_time = i / 2
        if cafe_list[count][0] <= current_time <= cafe_list[count][1]:
            if n != max_n and (current_time - 0.5).is_integer():
                n += 1
            if current_time == cafe_list[count][1] and count != m-1:
                count += 1
        elif (current_time - 0.5).is_integer():
            n -= 1
        if n == 0 and current_time != n or n < 0:
            print("No")
            sys.exit()
    print("Yes")

    """
