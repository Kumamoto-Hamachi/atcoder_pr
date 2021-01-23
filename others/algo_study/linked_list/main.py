class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

#    def __str__(self):
#        return f"""
#-value: {self.value} -next: {self.next} -prev: {self.prev}"""


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new = Cell(value)
        tmp = self.head
        # まだ一つも要素が無い場合
        if not tmp:
            self.head = new
            new.prev = new
            new.next = new
            return
        while not tmp == self.head:
            tmp = tmp.next
        # headの一つ前は必ず最後の要素になるので、最後の要素のnextに新しいcellを指定する
        tmp.prev.next = new # self.head(new1)をnew2にしてる？
        print("tmp.value", tmp.value)  # debug tmp.valueはずっと1のままになっている？！
        print("self.head", self.head.value)  # debug
        #self.head = new # loopする
        new.prev = tmp.prev # それってnewでは？
        new.next = tmp
        print("new.prev", new.prev.value)  # debug
        print("new.next", new.next.value)  # debug
        tmp.prev = new # tmpもnew、tmp.prevもnew

    def delete(self, value):
        tmp = self.head
        if not tmp:
            print("[*] List is empty.")
            return
        if tmp == tmp.next:
            self.head = tmp = None
            return
        if tmp.value == value:
            self.head = tmp.next
            tmp = None
            return
        isfound = False
        tmp = tmp.next
        while not tmp == self.head:
            if tmp.value == value:
                isfound = True
                break
            tmp = tmp.next
        if isfound:
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            tmp = None
        else:
            print("[*] Data not found")

    def show(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next
            if tmp == self.head:
                return
        else:
            print('[*] List is empty.')


if __name__ == "__main__":
    l = DoublyLinkedList()
    print('insert 1, 2, 3...')
    l.insert(1)
    l.insert(2)
    l.insert(3)
    print('print data')
    l.show()
    print('delete 2...')
    l.delete(1)
    print('print data')
    l.show()
    """
    input_str = snput()
    input_num = int(snput())
    some_map = m_snput()
    """
