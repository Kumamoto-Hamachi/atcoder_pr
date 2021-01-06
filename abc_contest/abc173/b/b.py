import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    c0, c1, c2, c3 = (0, 0, 0, 0)
    n = int(snput())
    count_list = [0] * 4
    # 若干ここの処理思いつくのに時間かかってた
    for i in range(n):
        result = snput()
        all_judge_type_list = ["AC", "WA", "TLE", "RE"]
        for i, t in enumerate(all_judge_type_list):
            if result == t:
                count_list[i] += 1
    for i, t in enumerate(all_judge_type_list):
        print(f"{t} x {count_list[i]}")

