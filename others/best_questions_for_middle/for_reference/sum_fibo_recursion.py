from itertools import permutations
import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def map_readline(): return map(int, readline().split())
def sreadline(): return readline().decode("utf-8").rstrip()

"""
Qiita:再帰関数を学ぶと、どんな世界が広がるか
https://qiita.com/drken/items/23a4f604fa3f505dd5ad
"""


# 再帰関数の中で再帰の呼び出しが1回の場合
def calc_sum_from(num):
    if num <= 0:  # ベースケースに対して return する処理を必ず入れる
        return 0
    sum_num = 0
    sum_num += num
    """
    再帰呼び出しを行ったときの問題が、
    元の問題よりも小さな問題となるように再帰呼び出しを行い、
    そのような「より小さい問題の系列」が最終的にベースケースに辿り着くようにする
    """
    sum_num += calc_sum_from(num-1)
    return sum_num

# 再帰関数の中で再帰の呼び出しが複数回の場合

# 0 1 1 2 3 5 8 13
def fibo_recursion(order):  # 計算量の爆発!!!
    num = 0
    if order == 0:
        return 0
    elif order == 1:
        return 1
    num += fibo(order-1) + fibo(order-2)
    return num


def fibo_for(order):  # 普通のfor文で
    first, second = 0, 1
    for i in range(order-1):
        first, second = second, first + second
        print("first, second", first, second)  # debug
    return second


memo = [-1] * 1000
def fibo(order):  # 動的計画法 or メモ化再帰
    if order == 0:
        return 0
    elif order == 1:
        return 1
    if memo[order] != -1:
        return memo[order]
    memo[order] = fibo(order-1) + fibo(order-2)
    return memo[order]


if __name__ == "__main__":
    n = 3
    """
    for i in range(11):
        ans = calc_sum_from(i)
        print(f"{i}までの和 = {ans}")
    """
    num = fibo(7)
    print("num", num)  # debug
