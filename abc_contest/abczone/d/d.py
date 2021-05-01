import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def main():
    S = sreadline()
    T = ""
    is_bottom = True
    kill_list = []
    for s in S:
        if s != "R":
            if len(T) == 0:
                T += s
            elif is_bottom:
                if T[-1] != s:
                    T += s
                else:
                    T = T[:-1]
            else:
                if T[0] != s:
                    T = s + T
                else:
                    T = T[1:]
        else:
            is_bottom = False if is_bottom else True
    if is_bottom:
        print(T)
    else:
        print(T[::-1])

if __name__ == "__main__":
    main()
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
