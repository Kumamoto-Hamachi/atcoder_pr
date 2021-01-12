import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())
PREFIX = "!"


class TwoSetManager:
    """This manager has headmark-set and no_headmark_set.
    He divides up input_str inot headmark or no-headmark"""

    class_name = "TwoSetManager"

    def __init__(self):
        self.headmark_set = set()
        self.no_headmark_set = set()

    def __str__(self):
        return f"class-name {self.__class__.class_name}"

    def check_opposite_partner(self, letter, headmark_flag):
        if headmark_flag:
            return (letter in self.no_headmark_set)
        else:
            return (letter in self.headmark_set)

    def add_affiliation_set(self, letter, headmark_flag):
        if headmark_flag:
            self.headmark_set.add(letter)
        else:
            self.no_headmark_set.add(letter)


if __name__ == "__main__":
    n = int(snput())
    two_set_manager = TwoSetManager()
    for _ in range(n):
        s = snput()
        headmark_flag = (s[0] == PREFIX)
        pure_letter = s[1:] if headmark_flag else s
        have_opposite_partner = two_set_manager.check_opposite_partner(pure_letter, headmark_flag)
        if have_opposite_partner:
            print(pure_letter)
            sys.exit()
        two_set_manager.add_affiliation_set(pure_letter, headmark_flag)
    print("satisfiable")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
