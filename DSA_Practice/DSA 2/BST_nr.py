class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def inorder(root):
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        result.append(curr.data)
        curr = curr.right

    return result

def preorder(root):
    result = []
    if root is None:
        return result

    stack = [root]

    while stack:
        curr = stack.pop()
        result.append(curr.data)

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return result

n = int(input())
arr = list(map(int, input().split()))

root = None

for x in arr[:n]:
    root = insert(root, x)

in_result = inorder(root)
pre_result = preorder(root)

print("Inorder Traversal:")
print(*in_result)

print("Preorder Traversal:")
print(*pre_result)