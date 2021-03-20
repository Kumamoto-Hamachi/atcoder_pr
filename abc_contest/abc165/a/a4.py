import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())

if __name__ == "__main__":
    K = int(readline())
    A, B = map_readline()
    print("OK" if B // K > (A - 1) // K else "NG")
    """
    K = int(readline())
    A, B = map_readline()
    under_a = (A // K) * K
    if under_a + K <= B or under_a == A:
        print("OK")
    else:
        print("NG")
    """

    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    sreadlines = [sb.decode("utf-8").rstrip() for sb in readlines()]
    """
