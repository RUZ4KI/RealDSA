class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        self.root = self.__insert_recursive(self.root,value)

    def __insert_recursive(self,node,value):
        if node is None:
            return Node(value)
        
        if value < node.value:
            node.left = self.__insert_recursive(node.left,value)

        elif value > node.value:
            node.right = self.__insert_recursive(node.right,value)

        return node
    
    def inorder(self):
        arr = []
        self.__inorder_recursive(self.root,arr)
        return arr
    
    def __inorder_recursive(self,node,arr):
        if node is None:
            return
        
        self.__inorder_recursive(node.left,arr)
        arr.append(node.value)
        self.__inorder_recursive(node.right,arr)

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
