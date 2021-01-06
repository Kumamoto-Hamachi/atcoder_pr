import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def execute_animal_num(animal_num, leg_num, crane_leg, turtle_leg):
    for i in range(animal_num+1):
        current_leg = crane_leg * i + turtle_leg * (animal_num - i)
        if current_leg == leg_num:
            return True
    return False

if __name__ == "__main__":
    animal_num, leg_num = m_snput()
    crane_leg = 2
    turtle_leg = 4
    # 処理としては無駄にfor文を回さないのはいいがもう少し綺麗に書けないか?
    if leg_num % 2 != 0:
        print("No")
    elif leg_num > animal_num * turtle_leg:
        print("No")
    # ここ長々しい
    elif execute_animal_num(animal_num, leg_num, crane_leg, turtle_leg):
        print("Yes")
    else:
        print("No")
