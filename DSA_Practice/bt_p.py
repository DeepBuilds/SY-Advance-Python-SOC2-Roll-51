class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
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
node=[]

b=BT()
for i in range(n):
  node.append(Node(values[i]))
for i in range(n):
  left=2*i +1
  right=2*i +2
  if left < n :
    node[i].left=node[left]
  if right < n:
    node[i].right=node[right]
root=node[0]
    
print("Inorder:- ",end="")
b.inorder(root)
print()
print("preorder:- ",end="")
b.preorder(root)
print()
print("postorder:- ",end="")
b.postorder(root)
print()