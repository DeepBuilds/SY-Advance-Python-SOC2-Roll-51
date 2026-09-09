class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BT:
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
            if root is not None:
                print(root.data,end=" ")
                self.preorder(root.left)
                self.preorder(root.right)
    def postorder(self,root):
            if root is not None:
                self.postorder(root.left)
                self.postorder(root.right)
                print(root.data,end=" ")
n = int(input())
values=input().split()
nodes=[]
bt=BT()
for i in range(n):
     nodes.append(Node(values[i]))
for i in range(n):
     
     left=2*i +1
     right=2*i +2

     if left<n:
          nodes[i].left=nodes[left]
     if right<n:
          nodes[i].right=nodes[right]
root=nodes[0]
print("Inorder: ",end="")
bt.inorder(root)
print()
root=nodes[0]
print("Preorder: ",end="")
bt.inorder(root)
print()
root=nodes[0]
print("Postorder: ",end="")
bt.postorder(root)
print() 