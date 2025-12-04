class Node :
   def __init__(self,value):
      self.prev = None
      self.value = value
      self.next = None

class DoublyLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0
      
   def insert_at_head(self,value):
      new_node = Node(value)
      new_node.next = self.head

      if self.head is not None:
         self.head.prev = new_node

      self.head = new_node

      if self.size == 0:
         self.tail = new_node
      
      self.size += 1
      
    
   def insert_at_tail(self,value):
      new_node = Node(value)
      new_node.prev = self.tail

      if self.tail is not None:
         self.tail.next = new_node
      
      self.tail = new_node

      if self.size == 0:
         self.head = new_node
      
      self.size += 1

   def search(self,value):
      curr = self.head
      while curr is not None:
         if curr.value == value:
            return True
         curr = curr.next
      return False

   def delete(self,value):
      if self.head == None:
         return
      
      if self.head.value == value:
         self.head = self.head.next
         if self.head is not None:
            self.head.prev = None
         else:
            self.tail = None
         self.size -=1
         return
      
      curr = self.head
      while curr:
         if curr.value == value:
            prev_node = curr.prev
            next_node = curr.next
            if next_node is not None:
               next_node.prev = prev_node
            if prev_node is not None:
               prev_node.next = next_node
            if next_node is None:
               self.tail = prev_node
            self.size -= 1
            return
         curr = curr.next

   def __str__(self):
      curr = self.head
      elements = []
      while curr:
         elements.append(str(curr.value))
         curr = curr.next
      print('->'.join(elements))


doublylinklist = DoublyLinkedList()
doublylinklist.insert_at_head(2)
doublylinklist.insert_at_head(3)
doublylinklist.insert_at_tail(4)
doublylinklist.delete(3)
doublylinklist