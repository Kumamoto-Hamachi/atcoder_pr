"""
DP Dynamic Programming:動的計画法
# Refer to https://www.youtube.com/watch?v=Ce8fWxzgi9Y
# Refer to https://www.youtube.com/watch?v=FBx54casFmQ
# Refer to https://qiita.com/drken/items/dc53c683d6de8aeacf5a

- ナップサック問題
# 関連：分子限定法,0-1ナップサック問題
[word]
    - 最適化問題(optimization problem):xの制約のもとで、yを最大(or最小)にするもの
    - 最適解(optimum solution):最適化問題で要求される出力
    - 目的関数(objective function):最適化問題の最大化(or最小化)の目的になっている関数
    ->ナップサック問題の場合は「ナップサックに詰めるアイテムの価値合計」
    - 最適値(optimum value):最適解の目的関数の値
    ->ナップサック問題の場合は「ナップサックに詰めるアイテムの価値合計」の最大値

[principle of optimality]
    - アイテムの大きさ合計c、価値合計をf(c)とする、またナップサックの最大容量をCとする
    - このとき、最適値 = max(f(0) ~ f(C))
    - ベルマン放程式(最適性原理)：これは漸化式なのでf(c)は再帰で計算できる
"""

if __name__ == "__main__":
    pass
