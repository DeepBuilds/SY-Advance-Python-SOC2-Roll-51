class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # Non-recursive Inorder
    def inorder(self):
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.data, end=" ")
            current = current.right

    # Non-recursive Preorder
    def preorder(self):
        if self.root is None:
            return

        stack = [self.root]

        while stack:
            current = stack.pop()
            print(current.data, end=" ")

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)


# Main program
bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.insert(value)

print("Inorder Traversal:")
bst.inorder()

print("\nPreorder Traversal:")
bst.preorder()