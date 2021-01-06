import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    n, m = m_snput()
    hw_list = m_snput()
    hw_day = sum(hw_list)
    play_day = n - hw_day
    if play_day < 0:
        print(-1)
    else:
        print(play_day)
