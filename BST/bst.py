class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        self.root = self._insert_recursive(self.root,value)

    def _insert_recursive(self,node,value):
        if node is None:
            return Node(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left,value)

        elif value > node.value:
            node.right = self._insert_recursive(node.right,value)

        return node
    
    def inorder(self):
        arr = []
        self._inorder_recursive(self.root,arr)
        return arr
    
    def _inorder_recursive(self,node,arr):
        if node is None:
            return
        
        self._inorder_recursive(node.left,arr)
        arr.append(node.value)
        self._inorder_recursive(node.right,arr)

    def preorder(self):
        arr = []
        self._preorder_recursive(self.root,arr)
        return arr
    
    def _preorder_recursive(self,node,arr):
        if node is None:
            return
        
        arr.append(node.value)
        self._preorder_recursive(node.left,arr)
        self._preorder_recursive(node.right,arr)

    def postorder(self):
        arr = []
        self._postorder_recursive(self.root,arr)
        return arr
    
    def _postorder_recursive(self,node,arr):
        if node is None:
            return
        
        self._postorder_recursive(node.left,arr)
        self._postorder_recursive(node.right,arr)
        arr.append(node.value)
    
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # -1 if height is edge based and 0 if height is nodes based
        return 1 + max(
            self._height_recursive(node.left),
            self._height_recursive(node.right)
            )

bst = BST()

print("Enter numbers for the BST. Type 'q' to stop.\n")

while True:
    user_input = input("Enter number: ")

    if user_input.lower() == "q":
        break

    try:
        num = int(user_input)
        bst.insert(num)
    except ValueError:
        print("Invalid input! Please enter an integer or 'q' to quit.")

print("\nInorder Traversal (sorted):")
print(bst.inorder())
print(bst.preorder())
print(bst.postorder())
print(bst.height())
