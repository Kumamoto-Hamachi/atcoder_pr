import sys
import array
snput = sys.stdin.buffer.readline
m_snput = lambda: map(int, snput().split())
"""
https://note.nkmk.me/python-list-array-numpy-ndarray/
Listはリファレンス実装であるCPythonではポインタを要素とする動的配列（dynamic array）。
連結リスト（linked list）ではない。
"""

if __name__ == "__main__":
    tmp_l = ["apple", 100, 0.123] # リスト
    arr_int = array.array("i", [0, 1, 2])
    for a in arr_int:
        print(a)
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
