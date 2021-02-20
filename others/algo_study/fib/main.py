memo = [0] * 1000
sequence = [1] * 1000


# 動的1
def fib(order):
    current_num = 1
    next_num = 1
    for i in range(order):
        increase = current_num
        current_num = next_num
        next_num += increase
    return current_num


# 動的2
def fib(order):
    current_num = 1
    next_num = 1
    for i in range(order):
        current_num, next_num = next_num, next_num + current_num
    return current_num


# 動的3
def fib(order):
    for i in range(2, order+1):
        sequence[i] = sequence[i-1] + sequence[i-2]
    return sequence[order]


# 再帰
def fib2(order):
    if order <= 1:
        return 1
    else:
        return fib2(order-1) + fib2(order-2)


# メモ化再帰
def fib3(order):
    if order <= 1:
        return 1
    else:
        if memo[order] == 0:
            memo[order] = fib3(order-1) + fib3(order-2)
        return memo[order]


if __name__ == "__main__":
    order = 4
    num = fib(order)
    print(num)
