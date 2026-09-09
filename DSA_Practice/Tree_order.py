class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
class BT:
  def inorder(self,root):
    if root is not None:
      self.inorder(root.left)
      print(root.data,sep='')
      self.inorder(root.right)
  def preorder(self,root):
    if root is not None:
      print(root.data,end="->")
      self.preorder(root.left)
      self.preorder(root.right)
  def postorder(self,root):
    if root is not None:
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end="->")
def main():
  t=BT()
  root=Node(1)
  root.left=Node(2)
  root.right=Node(3)
  root.left.left=Node(4)
  root.left.right=Node(5)
  root.right.left=Node(6)
  root.right.right=Node(7)
  print("\nInorder:-")
  t.inorder(root)
  print("\nPreorder:-")
  t.preorder(root)
  print("\nPostorder:-")
  t.postorder(root)
if __name__=="__main__":
  main()