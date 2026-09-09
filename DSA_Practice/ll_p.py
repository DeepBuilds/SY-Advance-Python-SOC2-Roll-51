class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LL:
  def __init__(self):
    self.head=None
  def insert(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      return "INSERT: "+data
    new_node.next=self.head
    self.head=new_node
    return "INSERT: "+data
  def insert_end(self,data):
    new_node=Node(data)
    if self.head is None :
      self.head=new_node
      return "INSERTED END: " + data
    temp=self.head
    while temp.next is not None:
      temp = temp.next
    temp.next= new_node
    return "Inserted end: "+data
  def display(self):
    temp=self.head
    result=[]
    while temp is not None:
      result.append(temp.data)
      temp=temp.next
    return "LIST: "+ " ".join(result)
ll=LL()
out=[]
n=int(input())
for i in range(n):
  op=input().split()
  if op[0]=="INSERTB":
    out.append(ll.insert(op[1]))
  elif op[0]=="INSERTE":
    out.append(ll.insert_end(op[1]))
  elif op[0]=="DISPLAY":
    out.append(ll.display())
for line in out:
  print(line)
    
    
  