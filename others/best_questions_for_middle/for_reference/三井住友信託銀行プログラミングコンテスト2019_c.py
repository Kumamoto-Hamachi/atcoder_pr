import sys
readline = sys.stdin.buffer.readline
def map_readline(): return map(int, readline().split())

# 動的計画法でも解くこと


if __name__ == "__main__":
    # 105円で抑え込める金額で100円で表現できる金額よりでかいならok!
    x = int(readline())
    for i in range(10 ** 3 + 1):
        if i * 100 <= x <= i * 105:
            print(1)
            sys.exit()
    print(0)

    """ 1つめの解答を理解するための別解 
    #5円以下なら一瞬で作れる.0円があるので数の調整は容易.
    #あとは数を制限以下に出来るかだけ
    computer_trifle = 105 % 100

    n = int(readline())
    items = n // 100
    rest_cost = n % 100

    computer_items = rest_cost // computer_trifle
    if rest_cost % computer_trifle != 0:
        computer_items += 1

    if computer_items <= items:
        print(1)
    else:
        print(0)
    """
