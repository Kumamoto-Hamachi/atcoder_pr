from pprint import pprint as pp
import sys
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()

if __name__ == "__main__":
    data = [['きゅうり',1,4],['いちご',2,6],['にんじん',2,1],['とうふ',1,0]]
    # 昇順でソート
    #sorted_data = sorted(data, key=lambda x:(x[1], x[2]))
    sorted_data = sorted(data, key=lambda x:(x[1], x[2]))
    reverse_data = sorted(data, key=lambda x:(x[1], x[2]), reverse=True)
    print(sorted_data)
    print(reverse_data)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    data = sreadline().split(" ")
    data = list(sreadline())
    """
