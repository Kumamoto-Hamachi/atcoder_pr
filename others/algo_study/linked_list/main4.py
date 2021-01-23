class Cell:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(value):
        new = Cell(value)
        # Listに何も無い時
        if self.head is None:
            self.head = new
            new.prev = new
            new.next = new
        # 更新
        # まず新しいcellを更新
        new.prev = self.head.prev
        new.next = self.head
        # 次にリストの旧頭の前と継続お尻の次のポインタ更新
        self.head.prev = new #旧頭の前は新頭となる新しく入ってきたcell
        self.head.prev.next = new # 継続お尻の次は新頭

    def insert_tail(value):
        new = Cell(value)
        # Listに何も無い時
        if self.head is None:
            self.head = new
            new.prev = new
            new.next = new
        # 更新
        # まず新しいcellを更新
        new.prev = self.head.prev
        new.next = self.head
        # 次にリストの継続頭の前と旧お尻の次のポインタ更新
        self.head.prev.next = new
        self.head.prev = new

    def delete(self, value):
        # 一つも要素が無い場合
        if self.head is None:
            sys.exit("List is empty")
        tmp_cell = self.head
        head_cell = self.head
        while tmp_cell:
            if tmp_cell.value == value:
                tmp_cell.prev.



