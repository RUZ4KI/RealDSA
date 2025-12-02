class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def insert_at_tail(self,value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def search(self,value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self,value):
        if self.head == None:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            self.size -= 1
            return
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                if curr is self.tail:
                    self.tail = prev
                self.size -= 1
                return
            prev = curr
            curr = curr.next