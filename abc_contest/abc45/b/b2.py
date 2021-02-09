import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()
MEMBER = 3


def get_person(card_collection, card_lens, person, i):
    if i <= card_lens[person]-1:
        person = card_collection[person][i]
    else:
        person = None
    return person


def judge_person(abc_orders, card_lens, person_l):
    for i in range(MEMBER):
        if abc_orders[i] > card_lens[person_l[i]]:
            return person_l[i]


# なんかブサイク、いくつもリストや辞書があるのが醜さの原因か？
if __name__ == "__main__":
    person_l = ["a", "b", "c"]
    card_collection = {"a":None, "b":None, "c":None}
    card_lens = {"a":None, "b":None, "c":None}
    for i in range(3):
        card_collection[person_l[i]] = list(sreadline())
        card_lens[person_l[i]] = len(card_collection[person_l[i]])
    person = "a"  # 初期値
    ai, bi, ci = 0, 0, 0  # 初期値
    while True:
        if person == "a":
            person = get_person(card_collection, card_lens, person, ai)
            ai += 1
        elif person == "b":
            person = get_person(card_collection, card_lens, person, bi)
            bi += 1
        elif person == "c":
            person = get_person(card_collection, card_lens, person, ci)
            ci += 1
        else:
            break
    abc_orders = [ai, bi , ci]
    person = judge_person(abc_orders, card_lens, person_l)
    print(person.upper())
    """
    input_str = readline()
    input_num = int(readline())
    some_map = map_readline()
    data = sreadline().split(" ")
    data = list(sreadline())
    """

