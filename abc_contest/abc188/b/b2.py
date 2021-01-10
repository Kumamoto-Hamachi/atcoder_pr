import sys
snput = lambda: sys.stdin.readline().rstrip()
m_snput = lambda: map(int, snput().split())

def calc_inner_prodocut(vector_a, vector_b):
    inner_product = 0
    for a, b in zip(vector_a, vector_b):
        inner_product += a * b
    return inner_product


if __name__ == "__main__":
    n = int(snput())
    vector_a = m_snput()
    vector_b = m_snput()
    inner_product = calc_inner_prodocut(vector_a, vector_b)
    if inner_product == 0:
        print("Yes")
    else:
        print("No")

    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
