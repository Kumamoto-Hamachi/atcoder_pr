import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class TwoWayLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        print("#" * 10)
        if self.head is None:
            sys.exit("List is empty")
        cursor = self.head
        while True:
            print(cursor.value)
            if cursor.next == self.head:
                break
            cursor = cursor.next

    def reverse_print(self):
        print("#" * 10)
        if self.head is None:
            sys.exit("List is empty")
        cursor = self.head.prev
        while True:
            print(cursor.value)
            if cursor.prev == self.head.prev:
                break
            cursor = cursor.prev

    def add_head(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.head.prev = node
            # node.prev = node
            self.head.next = node
            # node.next = node
            return
        # 新規追加データのポインタ更新
        node.prev = self.head.prev  # 新しい頭の前は既存の頭の前(継続お尻)
        node.next = self.head  # 新しい頭の次は既存の頭
        # リスト内の既存データのポインタ更新
        self.head.prev.next = node  # 継続お尻の次は頭
        self.head.prev = node  # 既存の頭の前は新しい頭
        self.head = node  # 頭の書き換え

    def add_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.head.prev = node
            # node.prev = node
            self.head.next = node
            # node.next = node
            return
        # 新規追加データのポインタ更新
        node.prev = self.head.prev  # 新しいお尻の前は旧お尻
        node.next = self.head  # 新しいお尻の次は既存の頭
        # リスト内の既存データのポインタ更新(self.tailがないからadd_headより書き換え少ない)
        self.head.prev.next = node  # 継続の頭の前(旧お尻)の次は新しいお尻
        self.head.prev = node  # 継続の頭の前は新しいお尻


if __name__ == "__main__":
    two_way_list = TwoWayLinkedList()
    two_way_list.add_head(1)
    two_way_list.print()
    two_way_list.add_head(2)
    two_way_list.print()
    two_way_list.add_head(3)
    two_way_list.print()
    two_way_list.add_head(4)
    two_way_list.print()
    two_way_list.add_tail(0)
    two_way_list.print()
    two_way_list.add_tail(1)
    two_way_list.print()
    two_way_list.reverse_print()
    two_way_list.add_tail(2)
    two_way_list.print()
