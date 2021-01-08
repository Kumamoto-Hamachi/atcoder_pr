import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def is_palindrome(s_str):
    for i, s in enumerate(reversed(s_str)):
        if not s_str[i] == s:
            print("No")
            sys.exit()

# コードが汚すぎる
if __name__ == "__main__":
    s_str = snput()
    n = len(s_str)
    is_palindrome(s_str)
    second_s = s_str[:(n-1)//2]
    is_palindrome(second_s)
    third_s = s_str[(n+3)//2-1:]
    is_palindrome(third_s)
    print("Yes")


    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
