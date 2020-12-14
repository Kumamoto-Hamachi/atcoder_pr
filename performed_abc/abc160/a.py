import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

if __name__ == "__main__":
    word = snput()
    if word[2] == word[3] and word[4] == word[5]:
        print("Yes")
    else:
        print("No")
