from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class MinHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)
        self.size += 1

        if not self.root:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            if not current.left:
                current.left = new_node
                new_node.parent = current
                break
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                new_node.parent = current
                break
            else:
                queue.append(current.right)

        self._bubble_up(new_node)

    def _bubble_up(self, node):
        while node.parent and node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    def delete_min(self):
        if not self.root:
            return None

        min_value = self.root.value

        if self.size == 1:
            self.root = None
            self.size = 0
            return min_value

        queue = deque([self.root])
        last = None

        while queue:
            last = queue.popleft()
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)

        self.root.value = last.value

        # Remove last node
        if last.parent.left == last:
            last.parent.left = None
        else:
            last.parent.right = None

        self.size -= 1

        self._bubble_down(self.root)

        return min_value

    def _bubble_down(self, node):
        while node:
            smallest = node

            if node.left and node.left.value < smallest.value:
                smallest = node.left

            if node.right and node.right.value < smallest.value:
                smallest = node.right

            if smallest == node:
                break

            node.value, smallest.value = smallest.value, node.value
            node = smallest

    def print_heap(self):
        if not self.root:
            print("Heap is empty")
            return

        queue = deque([self.root])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print(result)

heap = MinHeap()

heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(3)
heap.insert(8)

heap.print_heap()

print("Deleted:", heap.delete_min())
heap.print_heap()

print("Deleted:", heap.delete_min())
heap.print_heap()
