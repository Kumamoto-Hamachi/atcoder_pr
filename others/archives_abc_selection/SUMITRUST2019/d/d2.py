import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    N = int(readline())
    S = sreadline()
    possible_pins = [None] * 1000
    for i in range(1000):
        snum = str(i)
        possible_pins[i] = ("0" * (3 - len(snum)) + snum)
    pin_num = 0
    for pin in possible_pins:
        order = 0
        for s in S:
            order += (pin[order] == s)
            if order == 3:
                pin_num += 1
                break
    print(pin_num)
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
