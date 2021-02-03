import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
PREFIX = "!"


class TwoSetManager:

    def __init__(self):
        self.headmark = set()
        self.no_headmark = set()

    def check_opposite_partner(self, letter, headmark_flag):
        if headmark_flag:
            return (letter in self.no_headmark)
        else:
            return (letter in self.headmark)

    def add_affiliation_set(self, letter, headmark_flag):
        if headmark_flag:
            self.headmark.add(letter)
        else:
            self.no_headmark.add(letter)


if __name__ == "__main__":
    N = int(readline())
    two_set_manager = TwoSetManager()
    for _ in range(N):
        s = sreadline()
        headmark_flag = (s[0] == PREFIX)
        letter = s[1:] if headmark_flag else s
        check_opposite_partner = two_set_manager.check_opposite_partner(letter, headmark_flag)
        if check_opposite_partner:
            print(letter)
            sys.exit()
        two_set_manager.add_affiliation_set(letter, headmark_flag)
    print("satisfiable")
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
