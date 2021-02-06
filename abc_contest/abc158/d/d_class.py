import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline
map_readline = lambda: map(int, readline().split())
sreadline = lambda: readline().decode("utf-8").rstrip()


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.head.prev = node
            self.head.next = node
            return
        # 新規追加nodeのポインタ更新
        node.prev = self.head.prev
        node.next = self.head
        # 既存nodeのポインタ更新
        self.head.prev.next = node  # TODOこういうところでミスったときのデバッグ方法
        self.head.prev = node
        self.head = node

    def add_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.head.prev = node
            self.head.next = node
            return
        # 新規追加nodeのポインタ更新
        node.next = self.head
        node.prev = self.head.prev
        # 既存nodeのポインタ更新
        self.head.prev.next = node
        self.head.prev = node

    def print(self):
        if self.head is None:
            sys.exit("List is empty")
        cursor = self.head
        while True:
            print(cursor.value, end="")
            cursor = cursor.next
            if cursor == self.head:
                break

    def reverse_print(self):
        if self.head is None:
            sys.exit("List is empty")
        cursor = self.head.prev
        while True:
            print(cursor.value, end="")
            cursor = cursor.prev
            if cursor == self.head.prev:
                break


if __name__ == "__main__":
    two_way_list = DoubleLinkedList()
    origin_str = sreadline()
    for s in origin_str:  # MISS POINT
        two_way_list.add_tail(s)
        # two_way_list.print()
    Q = int(readline())
    reverse_flag = False
    for _ in range(Q):
        query = sreadline().split()
        if query[0] == "1":
            reverse_flag = True if not reverse_flag else False
        else:
            top_or_bottom = int(query[1])  # top == 1 bottom == 2
            new_s = query[2]
            if (reverse_flag + top_or_bottom) % 2 == 1:
                two_way_list.add_head(new_s)
            else:
                two_way_list.add_tail(new_s)
    if reverse_flag:
        two_way_list.reverse_print()
    else:
        two_way_list.print()
