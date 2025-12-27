from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class TreeHeap:
    def __init__(self, root):
        self.root = root

    def heapify(self):
        if not self.root:
            return

        nodes = []
        q = deque([self.root])

        while q:
            node = q.popleft()
            nodes.append(node)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        last_internal = (len(nodes) // 2) - 1

        for i in range(last_internal, -1, -1):
            self._bubble_down(nodes[i])


    def _bubble_down(self, node):
        while True:
            smallest = node

            if node.left and node.left.value < smallest.value:
                smallest = node.left
            if node.right and node.right.value < smallest.value:
                smallest = node.right

            if smallest == node:
                break

            node.value, smallest.value = smallest.value, node.value
            node = smallest


root = Node(20)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(22)
root.left.right = Node(9)
root.right.left = Node(13)

heap = TreeHeap(root)
heap.heapify()

print(root.value) 

