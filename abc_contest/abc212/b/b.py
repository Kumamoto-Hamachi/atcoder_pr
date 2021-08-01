import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

def is_weak(password):
    for i in range(3):
        first = int(password[i])
        second = int(password[i+1])
        if first + 1 != second and not (first == 9 and second == 0):
            return False
    return True

if __name__ == "__main__":
    password = list(map(int, sreadline()))
    if len(set(password)) == 1:
        print("Weak")
    elif is_weak(password):
        print("Weak")
    else:
        print("Strong")
