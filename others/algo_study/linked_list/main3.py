import sys

class Cell:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new = Cell(value)
        # 一つも要素が無い時
        if self.head is None:
            self.head = new
            new.prev = new
            new.next = new
        # まずは新しく入ってくる要素のポインタ付与
        new.next = self.head
        new.prev = self.head.prev
        # TODO 次にリストの更新 最後の次と二番目の要素の前、頭を変える
        # かつてのheadの前の要素は最後、最後の次は次は新しいcell
        self.head.prev.next = new
        # かつてのheadの前の要素は新しいcell
        self.head.prev = new
        # 頭は新しいcellに
        self.head = new

    def insert_tail(self, value):
        new = Cell(value)
        # 一つも要素が無い時
        if self.head is None:
            self.head = new
            self.head.prev = new
            self.head.next = new
        # まず新しいcellを更新
        new.next = self.head # 新しいお尻の次は今の頭
        new.prev = self.head.prev #新しいお尻の前は前のお尻
        # 次にリスト内の頭と旧式お尻の要素のポインタ更新
        self.head.prev.next = new # 旧お尻のポインタ更新
        self.head.prev = new # (継続している)頭の要素のポインタ更新
