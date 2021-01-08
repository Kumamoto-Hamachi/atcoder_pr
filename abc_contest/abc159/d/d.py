import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())


if __name__ == "__main__":
    N = int(snput())
    A = list(m_snput())
    c = [0] * (N+1)
    for a in A:
        c[a] += 1
    s = sum(x*(x-1)//2 for x in c)
    for a in A:
        print(s-(c[a]-1))
    """
    https://atcoderblue.asukatagui-blog.com/abc159d/
    input_str = snput()
    some_map = m_snput()
    """
