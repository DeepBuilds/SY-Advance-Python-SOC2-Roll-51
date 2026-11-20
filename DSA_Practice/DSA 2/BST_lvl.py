from collections import deque
class Node:
  def __init__(self,id):
    self.id=id
    self.left=None
    self.right=None
def insert(root,id):
  if root is None:
    return Node(id)
  if id <root.id:
    root.left=insert(root.left,id)
  else:
    root.right=insert(root.right,id)
  return root
def lvl(root):
  result=[]
  if root is None:
    return result
  q=deque([root])
  while q:
    levels=[]
    for i in range(len(q)):
      cur=q.popleft()
      levels.append(cur.id)
      if cur.left:
        q.append(cur.left)
      if cur.right:
        q.append(cur.right)
    result.append(levels)
  return result
def height(root):
  if root is None:
    return 0
  return 1+ max(height(root.left),height(root.right))
def leaf(root):
  leaves=[]
  
  if  root:
    if root.left is None and root.right is None:
      leaves.append(root.id)
    leaves.extend(leaf(root.left))
    leaves.extend(leaf(root.right))
  return leaves
n=int(input())
arr=list(map(int,input().split()))
root=None
for i in arr[:n]:
  root=insert(root,i)
lvls=lvl(root)
h=height(root)
leafs=leaf(root)
print("Level:-")
for i in lvls:
  print(*i)
print('height:-',h)
print("leaves:-")
for i in leafs:
  print(i)
      